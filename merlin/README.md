# generate wav using mgc bap lf0
put run_generate.sh to merlin/egs/yourvoice/s1/
put generate_wav.py to merlin/src/

put your mgc lf0 bap to
merlin/egs/yourvoice/s1/experiments/yourvoice/test_synthesis/wav

then run 
```
./run_generate.sh conf/test_synth_config_file
```

you will get your wav in 
merlin/egs/yourvoice/s1/experiments/yourvoice/test_synthesis/wav
