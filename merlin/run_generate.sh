#!/bin/bash -e

global_config_file=conf/global_settings.cfg
source $global_config_file

test_synth_config_file=$1

echo "synthesizing speech..."
./scripts/submit.sh ${MerlinDir}/src/generate_wav.py $test_synth_config_file
python ${MerlinDir}/src/generate_wav.py $test_synth_config_file



