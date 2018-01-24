# MTTS 中文语音合成

**ON_DEVELOPMENT**

Mandarin/Chinese Text to Speech based on statistical parametric speech synthesis using merlin toolkit

[中文语音合成手册（整理中）](http://mtts.readthedocs.io/zh_CN/latest/#)  
[中文语音合成相关思维导图（更新中）](http://naotu.baidu.com/file/efd4f580e80ed57c7bef115f2d7d5813?token=9b6dd5d2e4bc5b95)  

目前实现了简单的自动文本转label程序，设计了上下文相关标注格式和对应的问题集，具体见misc文件夹。

如果你想要实现中文语音合成，需要有自己的语料库（目前网络上没有开源的中文语音合成语料库）——文本，音频，韵律标注（也可以不要），音素发音时长标注，然后生成Label文件，在merlin下训练即可

目前用1600中文短句训练的效果见example_wav，音质不好，但能辨别出读的什么字，用更大的数据量应该可以取得更好的效果

## TODO List
* Forced Alignment 根据音频文件和文本生成发音时长标注
* 测试在更大规模数据中的效果

## 使用指南
### 1.txt2label

```
from mandarin_frontend import txt2label

result = txt2label('香港和澳门')
for line in result:
    print(line)

# 带韵律标记的文本也被支持
# result = txt2label('香港#1和#1澳门')

# 可加入发音时长文件
# result = txt2label('香港和澳门', sfsfile='example.sfs')
```

生成Label如下
```
0 0 xx^xx-sil+x=iang1@/A:xx-xx^xx@/B:xx+xx@xx^xx^xx+xx#xx-xx-/C:xx_xx^xx#xx+xx+xx&/D:xx=xx!xx@xx-xx&/E:xx|xx-xx@xx#xx&xx!xx-xx#/F:xx^xx=xx_xx-xx!
0 0 xx^sil-x+iang1=g@/A:xx-1^3@/B:0+4@1^2^1+5#1-5-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 sil^x-iang1+g=ang3@/A:xx-1^3@/B:0+4@1^2^1+5#1-5-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 x^iang1-g+ang3=h@/A:1-3^2@/B:1+3@2^1^2+4#2-4-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 iang1^g-ang3+h=e2@/A:1-3^2@/B:1+3@2^1^2+4#2-4-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 g^ang3-h+e2=ao4@/A:3-2^4@/B:2+2@1^1^3+3#3-3-/C:n_c^n#2+1+2&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 ang3^h-e2+ao4=m@/A:3-2^4@/B:2+2@1^1^3+3#3-3-/C:n_c^n#2+1+2&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 h^e2-ao4+m=en2@/A:2-4^2@/B:3+1@1^2^4+2#4-2-/C:c_n^xx#1+2+xx&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 e2^ao4-m+en2=sil@/A:4-2^xx@/B:4+0@2^1^5+1#5-1-/C:c_n^xx#1+2+xx&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 ao4^m-en2+sil=xx@/A:4-2^xx@/B:4+0@2^1^5+1#5-1-/C:c_n^xx#1+2+xx&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 m^en2-sil+xx=xx@/A:xx-xx^xx@/B:xx+xx@xx^xx^xx+xx#xx-xx-/C:xx_xx^xx#xx+xx+xx&/D:xx=xx!xx@xx-xx&/E:xx|xx-xx@xx#xx&xx!xx-xx#/F:xx^xx=xx_xx-xx!
```

### 2.merlin脚本
将egs/mandarin_voice复制到merlin对应文件夹下，然后根据egs/mandarin_voice/s1/README.md进行配置即可


## 贡献者：
* Jackiexiao
* willian56

