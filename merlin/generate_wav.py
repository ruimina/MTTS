import configuration
from utils.file_paths import FilePaths
import sys, os, subprocess, glob, subprocess
from io_funcs.binary_io import  BinaryIOCollection
import numpy as np
import logging
import logging.config
from logplot.logging_plotting import LoggerPlotter, MultipleSeriesPlot, SingleWeightMatrixPlot

def generate_wav(gen_dir, file_id_list, cfg):

    logger = logging.getLogger("wav_generation")

    ## STRAIGHT or WORLD vocoders:
    wavgen_straight_type_vocoder(gen_dir, file_id_list, cfg, logger)
    return

def wavgen_straight_type_vocoder(gen_dir, file_id_list, cfg, logger):
    '''
    Waveform generation with STRAIGHT or WORLD vocoders.
    (whose acoustic parameters are: mgc, bap, and lf0)
    '''

    SPTK     = cfg.SPTK
#    NND      = cfg.NND
    STRAIGHT = cfg.STRAIGHT
    WORLD    = cfg.WORLD

    ## to be moved
    pf_coef = cfg.pf_coef
    if isinstance(cfg.fw_alpha, str):
        if cfg.fw_alpha=='Bark':
            fw_coef = bark_alpha(cfg.sr)
        elif cfg.fw_alpha=='ERB':
            fw_coef = bark_alpha(cfg.sr)
        else:
            raise ValueError('cfg.fw_alpha='+cfg.fw_alpha+' not implemented, the frequency warping coefficient "fw_coef" cannot be deduced.')
    else:
        fw_coef = cfg.fw_alpha
    co_coef = cfg.co_coef
    fl_coef = cfg.fl

    counter=1
    max_counter = len(file_id_list)

    for filename in file_id_list:

        logger.info('creating waveform for %4d of %4d: %s' % (counter,max_counter,filename) )
        counter=counter+1
        base   = filename
#        files = {'sp'  : base + cfg.sp_ext,
#                 'mgc' : base + cfg.mgc_ext,
#                 'f0'  : base + '.f0',
#                 'lf0' : base + cfg.lf0_ext,
#                 'ap'  : base + '.ap',
#                 'bap' : base + cfg.bap_ext,
#                 'wav' : base + '.wav'}
#
        files = {'sp'  : base + '.sp',
                 'mgc' : base + '.mgc',
                 'f0'  : base + '.f0',
                 'lf0' : base + '.lf0',
                 'ap'  : base + '.ap',
                 'bap' : base + '.bap',
                 'wav' : base + '.wav'}


        mgc_file_name = files['mgc']
        bap_file_name = files['bap']

        cur_dir = os.getcwd()
        os.chdir(gen_dir)

#        ### post-filtering
#        if cfg.do_post_filtering:
#            mgc_file_name = files['mgc']+'_p_mgc'
#            post_filter(files['mgc'], mgc_file_name, cfg.mgc_dim, pf_coef, fw_coef, co_coef, fl_coef, gen_dir, cfg)
#
        ###mgc to sp to wav
        run_process('{sopr} -magic -1.0E+10 -EXP -MAGIC 0.0 {lf0} | {x2x} +fd > {f0}'.format(sopr=SPTK['SOPR'], lf0=files['lf0'], x2x=SPTK['X2X'], f0=files['f0']))

        run_process('{sopr} -c 0 {bap} | {x2x} +fd > {ap}'.format(sopr=SPTK['SOPR'],bap=files['bap'],x2x=SPTK['X2X'],ap=files['ap']))

        ### If using world v2, please comment above line and uncomment this
        #run_process('{mgc2sp} -a {alpha} -g 0 -m {order} -l {fl} -o 0 {bap} | {sopr} -d 32768.0 -P | {x2x} +fd > {ap}'
        #            .format(mgc2sp=SPTK['MGC2SP'], alpha=cfg.fw_alpha, order=cfg.bap_dim, fl=cfg.fl, bap=bap_file_name, sopr=SPTK['SOPR'], x2x=SPTK['X2X'], ap=files['ap']))

        run_process('{mgc2sp} -a {alpha} -g 0 -m {order} -l {fl} -o 2 {mgc} | {sopr} -d 32768.0 -P | {x2x} +fd > {sp}'
                    .format(mgc2sp=SPTK['MGC2SP'], alpha=cfg.fw_alpha, order=cfg.mgc_dim-1, fl=cfg.fl, mgc=mgc_file_name, sopr=SPTK['SOPR'], x2x=SPTK['X2X'], sp=files['sp']))

        run_process('{synworld} {fl} {sr} {f0} {sp} {ap} {wav}'
                     .format(synworld=WORLD['SYNTHESIS'], fl=cfg.fl, sr=cfg.sr, f0=files['f0'], sp=files['sp'], ap=files['ap'], wav=files['wav']))

        run_process('rm -f {ap} {sp} {f0}'.format(ap=files['ap'],sp=files['sp'],f0=files['f0']))

        os.chdir(cur_dir)



def run_process(args,log=True):

    logger = logging.getLogger("subprocess")

    # a convenience function instead of calling subprocess directly
    # this is so that we can do some logging and catch exceptions

    # we don't always want debug logging, even when logging level is DEBUG
    # especially if calling a lot of external functions
    # so we can disable it by force, where necessary
    if log:
        logger.debug('%s' % args)

    try:
        # the following is only available in later versions of Python
        # rval = subprocess.check_output(args)

        # bufsize=-1 enables buffering and may improve performance compared to the unbuffered case
        p = subprocess.Popen(args, bufsize=-1, shell=True,
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        close_fds=True, env=os.environ)
        # better to use communicate() than read() and write() - this avoids deadlocks
        (stdoutdata, stderrdata) = p.communicate()

        if p.returncode != 0:
            # for critical things, we always log, even if log==False
            logger.critical('exit status %d' % p.returncode )
            logger.critical(' for command: %s' % args )
            logger.critical('      stderr: %s' % stderrdata )
            logger.critical('      stdout: %s' % stdoutdata )
            raise OSError

        return (stdoutdata, stderrdata)

    except subprocess.CalledProcessError as e:
        # not sure under what circumstances this exception would be raised in Python 2.6
        logger.critical('exit status %d' % e.returncode )
        logger.critical(' for command: %s' % args )
        # not sure if there is an 'output' attribute under 2.6 ? still need to test this...
        logger.critical('  output: %s' % e.output )
        raise

    except ValueError:
        logger.critical('ValueError for %s' % args )
        raise

    except OSError:
        logger.critical('OSError for %s' % args )
        raise

    except KeyboardInterrupt:
        logger.critical('KeyboardInterrupt during %s' % args )
        try:
            # try to kill the subprocess, if it exists
            p.kill()
        except UnboundLocalError:
            # this means that p was undefined at the moment of the keyboard interrupt
            # (and we do nothing)
            pass

        raise KeyboardInterrupt


def bark_alpha(sr):
    return 0.8517*np.sqrt(np.arctan(0.06583*sr/1000.0))-0.1916

def erb_alpha(sr):
    return 0.5941*np.sqrt(np.arctan(0.1418*sr/1000.0))+0.03237

def post_filter(mgc_file_in, mgc_file_out, mgc_dim, pf_coef, fw_coef, co_coef, fl_coef, gen_dir, cfg):

    SPTK = cfg.SPTK

    line = "echo 1 1 "
    for i in range(2, mgc_dim):
        line = line + str(pf_coef) + " "

    run_process('{line} | {x2x} +af > {weight}'
                .format(line=line, x2x=SPTK['X2X'], weight=os.path.join(gen_dir, 'weight')))

    run_process('{freqt} -m {order} -a {fw} -M {co} -A 0 < {mgc} | {c2acr} -m {co} -M 0 -l {fl} > {base_r0}'
                .format(freqt=SPTK['FREQT'], order=mgc_dim-1, fw=fw_coef, co=co_coef, mgc=mgc_file_in, c2acr=SPTK['C2ACR'], fl=fl_coef, base_r0=mgc_file_in+'_r0'))

    run_process('{vopr} -m -n {order} < {mgc} {weight} | {freqt} -m {order} -a {fw} -M {co} -A 0 | {c2acr} -m {co} -M 0 -l {fl} > {base_p_r0}'
                .format(vopr=SPTK['VOPR'], order=mgc_dim-1, mgc=mgc_file_in, weight=os.path.join(gen_dir, 'weight'),
                        freqt=SPTK['FREQT'], fw=fw_coef, co=co_coef,
                        c2acr=SPTK['C2ACR'], fl=fl_coef, base_p_r0=mgc_file_in+'_p_r0'))

    run_process('{vopr} -m -n {order} < {mgc} {weight} | {mc2b} -m {order} -a {fw} | {bcp} -n {order} -s 0 -e 0 > {base_b0}'
                .format(vopr=SPTK['VOPR'], order=mgc_dim-1, mgc=mgc_file_in, weight=os.path.join(gen_dir, 'weight'),
                        mc2b=SPTK['MC2B'], fw=fw_coef,
                        bcp=SPTK['BCP'], base_b0=mgc_file_in+'_b0'))

    run_process('{vopr} -d < {base_r0} {base_p_r0} | {sopr} -LN -d 2 | {vopr} -a {base_b0} > {base_p_b0}'
                .format(vopr=SPTK['VOPR'], base_r0=mgc_file_in+'_r0', base_p_r0=mgc_file_in+'_p_r0',
                        sopr=SPTK['SOPR'],
                        base_b0=mgc_file_in+'_b0', base_p_b0=mgc_file_in+'_p_b0'))

    run_process('{vopr} -m -n {order} < {mgc} {weight} | {mc2b} -m {order} -a {fw} | {bcp} -n {order} -s 1 -e {order} | {merge} -n {order2} -s 0 -N 0 {base_p_b0} | {b2mc} -m {order} -a {fw} > {base_p_mgc}'
                .format(vopr=SPTK['VOPR'], order=mgc_dim-1, mgc=mgc_file_in, weight=os.path.join(gen_dir, 'weight'),
                        mc2b=SPTK['MC2B'],  fw=fw_coef,
                        bcp=SPTK['BCP'],
                        merge=SPTK['MERGE'], order2=mgc_dim-2, base_p_b0=mgc_file_in+'_p_b0',
                        b2mc=SPTK['B2MC'], base_p_mgc=mgc_file_out))

    return


if __name__ == '__main__':
    config_file = sys.argv[1]
    config_file = os.path.abspath(config_file)
    cfg=configuration.cfg
    cfg.configure(config_file)
    file_paths = FilePaths(cfg)
    test_id_list = file_paths.test_id_list
    gen_file_id_list = test_id_list
    gen_dir = cfg.test_synth_dir
    generate_wav(gen_dir, gen_file_id_list, cfg)     # generated speech

