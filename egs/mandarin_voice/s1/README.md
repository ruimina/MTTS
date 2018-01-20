# Mandarin Voice

(1) Copy your file to 

* database/wav 
* database/labels/label_phone_align 
* database/prompt-lab 


(2) modify params as per your own data in 01_setup.sh file, especially

* QuestionFile
* Labels
* SamplingFreq
* Train
* Valid
* Test

default setting is 

* QuestionFile=questions-mandarin.hed
* Labels=phone_align
* SamplingFreq=44100
* Train=40
* Valid=5
* Test=5



(3) then run

```
./run_king_voice.sh
```
