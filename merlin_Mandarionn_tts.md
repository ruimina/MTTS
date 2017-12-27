# Merlin:中文统计参数语音合成实战

本文目标是详细解释如何基于开源Merlin项目搭建中文统计参数语音合成系统，但笔者目前尚未实现中文语音合成，实现中文语音合成系统将作为笔者的毕业设计，本文记录了笔者的进展并且会持续更新直到实现中文语音合成为止。  

[中文语音合成相关思维导图（更新中）](http://naotu.baidu.com/file/efd4f580e80ed57c7bef115f2d7d5813?token=9b6dd5d2e4bc5b95)  

更新时间：2017-11-22  
有意交流语音合成研究可加微信explorerrr

目录

 * [目前研究进展](#目前研究进展)
 * [Merlin的安装与运行](#merlin的安装与运行) 
 * [Merlin开源代码的学习](#merlin开源代码的学习)
 * [英文语音合成理论研究](#英文语音合成理论研究)
 * [英文语音合成实现](#英文语音合成实现)
 * [中文语音合成理论研究](#中文语音合成理论研究)
 * [中文语音合成实现](#中文语音合成实现)
 * [附录](#附录)
 * [术语表](#术语表)
 * [联系作者](#联系作者)

# 目前研究进展

百度Deep Voice

Deep Voice在发音前先将文字转化为音素（最小的语音单位），然后再依靠自己的语音合成网络将其变为你所听到的声音。该系统包含 5 个重要基础：定位音素边界的分割模型、字母到音素的转换模型、音素时长预测模型、基础频率预测模型、音频合成模型。为了更好的表达情感，需要人为的控制音素、音节的加重、缩短以及拖长。

 在几乎无须人工介入的前提下，只需短短数小时便能学会说话。开发人员还可以对其要传达的感情状态进行设定，这样合成出来的语音听起来就会非常真实、自然。

DeepMind WaveNet

WaveNet采用的是参量式TTS模型，通过直接将音频信号的原始波形进行建模，并且一次产生一个样本，通过vocoders的信号处理算法来输出它的结果，以生成语音信号。此外，使用原始波形，意味着WaveNet可以对包括音乐在内的任何音频进行建模，这样子生成的语音听起来会更自然。

WaveNet是一个完全的卷积神经网络。在这其中，卷积层拥有不同的扩张因素，能够让它的接受域随着成千上万的timesteps的深度和覆盖呈现指数型的增长。

在训练时，输入序列是来自人类演讲者的真实的波形。在训练后，我们可以取样这个网络来生成合成的语音。每一步的采样值是由网络计算得出的概率分布得到的。这个值随后会重新回到输入端，然后在下一步生成一个新的预测。构建一个像这样能够一次进行一步取样的网络是需要大量的计算的，所以在效率方面是WaveNet比较头痛的问题。

使用的开源库：Merlin语音合成系统

# Merlin的安装与运行

## 1.基础知识

Merlin只能在unix类系统下运行，使用Python2.7，并用theano作为后端，因此在使用Merlin之前，至少需要如下基础

- 熟练掌握linux系统，熟悉shell脚本
- 掌握python，了解常用Python库的使用
- 掌握theano
- 机器学习基础知识
- 语音识别和语音合成的知识

熟练地掌握上述知识需要花费大量的时间。在文章的末尾，我们会贴出我们所使用/推荐的学习资料。

## 2.安装Merlin

Merlin的Python语言采用的是Python2.7编写，所以我们需要在Python2.7的环境下运行Merlin，为避免python不同版本之间的冲突，我们采用Anaconda对Python运行环境进行管理。  
使用Anaconda创建Merlin运行环境具体操作如下：  
打开终端，使用下面命令查看一下现有python环境  
`conda env list`  
使用下面命令创建一个名为merlin的python环境  
`conda create --name merlin python=2.7`
先进入merlin环境中  
`source activate merlin`
在这个环境下安装merlin  
```
sudo apt-get install csh
pip install numpy scipy matplotlib lxml theano bandmat
git clone https://github.com/CSTR-Edinburgh/merlin.git
cd merlin/tools
./compile_tools.sh
```
如果一切顺利，此时你已经成功地安装了Merlin，但要注意的是Merlin不是一个完整的TTS系统。它提供了核心的声学建模功能：语言特征矢量化，声学和语言特征归一化，神经网络声学模型训练和生成。但语音合成的前端（文本处理器）以及声码器需要另外配置安装。此外，Merlin目前仅提供了英文的语音合成。  
此外，上述安装默认只配置支持CPU的theano，如果想要用GPU加速神经网络的训练，还需要进行其他的步骤。由于语料库的训练时间尚在笔者的接受范围之内（intel-i5，训练slt_arctic_full data需要大概6个小时），因此这里并没有使用GPU进行加速训练。  

## 3.运行Merlin demo
`.～/merlin/egs/slt_arctic/s1/run_demo.sh`
该脚本会使用50个音频样本进行声学模型和durarion模型的训练，并合成5个示例音频。在此略去详细的操作步骤，具体可参见：Getting started with the Merlin Speech Synthesis Toolkit [installing-Merlin](https://jrmeyer.github.io/merlin/2017/02/14/Installing-Merlin.html)  

# Merlin开源代码的学习
## 0 文件含义

Folder        |    Contains
------------- | -------------------
recordings    |     speech recordings, copied from the studio
wav           |     individual wav files for each utterance
pm            |     pitch marks
mfcc          |     MFCCs for use in automatic alignment[mfcc tutorial](http://practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)
lab           |     label files from automatic alignment
utt           |     Festival utterance structures
f0            |     Pitch contours
coef          |     MFCCs + f0, for the join cost
coef2         |     coef2, but stripped of unnecessary frames to save space, for the join cost
lpc           |     LPCs and residuals, for waveform generation
bap           |     band aperiodicity

1 免费的语料库

Merlin使用了网络上免费的语料库slt_arctic，可以在以下网址进行下载：[slt_arctic_full_data.zip](http://104.131.174.95/slt_arctic_full_data.zip)

2 训练数据的处理

Merlin自带的demo（merlin/egs/slt_arctic/s1 ）已经事先完成了label文件的提取，所以这里不需要前端FrontEnd对数据进行处理。  
Merlin通过脚本文件setup.sh在～/merlin/egs/slt_arctic/s1 目录下创建目录experiments，在experiments目录下创建目录slt_arctic_demo，完成数据的下载与解压，并将解压后的数据分别放到slt_arctic_demo/acoustic_mode/data，slt_arctic_demo/duration_model/data目录下，分别用于声学模型和持续时间模型的训练。

3 Demo语料库的训练

run_demo.sh文件会进行语音的训练以及合成。这里有许多的工程实现细节，在这里略去说明，其主要进行了如下步骤
![img](/img/image5.png)
其中语料库包含了文本和音频文件，文本需要首先通过前端FrontEnd处理成神经网络可接受的数据，这一步比较繁琐，不同语言也各不相同，下面会着重讲解。音频文件则通过声码器（这里使用的是STRAIGHT声码器）转换成声码器参数（包括了mfcc梅谱倒谱系数，f0基频，bap：band aperiodicity等）再参与到神经网络的训练之中。

4 Demo语料库的合成

Demo中提供了简单的合成方法，使用demo（merlin/egs/slt_arctic/s1 ）下的脚本文件：merlin_synthesis.sh即可进行特定文本的语音合成。  
同样的，由于merlin没有自带frontend，所以其demo中直接使用了事先经过frontend转换的label文件作为输入数据来合成语音。如果想要直接输入txt文本来获得语音，需要安装FrontEnd（下文会提及）并根据merlin_synthesis.sh文件的提示用FrontEnd来转换txt文本成label文件，再进行语音合成。  
对于英文语音合成，merlin中需要首先通过Duration模型确定音素的发音时间，然后根据声学模型合成完整的语音。  

5.Merlin的训练网络

Merlin的训练网络可见[*Merlin: An Open Source Neural Network Speech Synthesis System *](http://ssw9.net/papers/ssw9_PS2-13_Wu.pdf)  
Merlin一共提供了4类神经网络用于HMM模型的训练，分别是  
- 前馈神经网络
- 基于LSTM的RNN网络
- 双向RNN网络
- 其他变体（如blstm）

# 英文语音合成理论研究

如“基于HMM模型的语音合成系统”图片所示，英文语音合成分成训练和合成阶段，而训练阶段又由以下几个步骤组成

- 文本分析——对应FrontEnd
- HMM模型聚类——对应Question File
- 音频特征参数提取——对应Vocoder
- HMM模型训练——对应HMM模型训练

合成阶段则包括

- HMM解码——对应HMM模型训练
- 文本分析——对应FrontEnd
- 语音合成——对应Vocoder


HMM模型大致如下图所示
![img](/img/image2.png)
![img](/img/image3.png)

由于网上已有大量关于HMM模型的介绍，而且由于篇幅所限，本文不对HMM模型进行详细的说明。

![img](/img/image4.png)

训练过程中的文本分析和音频特征参数提取

## 0 文本与音频
语料库通常包含基本的txt和wav文件，而是否提供更多的信息如发音，拼音标注，分词，韵律结构，发音时长等每个语料库都不一样。
我们通常需要知道每个音节/音素对应的wav片段以及持续时间是多少，给定一段文本，标注它在音频中的准确位置的任务就叫force-alignment，这里有[forced-alignment-tools](https://github.com/pettarin/forced-alignment-tools)  
从其中可知[aeneas](https://www.readbeyond.it/aeneas/) 是支持中文简体和繁体的alignment的


## 1 前端FrontEnd 

关于英文FrontEnd设计可参考：[front-end Design](http://research.cs.tamu.edu/prism/lectures/sp/l17.pdf),这个pdf大概讲解了frontend的基础架构，frontend的设计需要大量的语言学知识，工作相对也是比较繁琐的。(the front-end provides a symbolic linguistic representation of the text in terms of phonetic transcription and prosody information)
语音合成前端（Front-End）实际上是一个文本分析器，属于 NLP(Natural Language Processing)的研究范畴，其目的是  

 - 对输入文本在语言层、语法层、语义层的分析
 - 将输入的文本转换成层次化的语音学表征
     - 包括读音、分词、短语边界、轻重读等 
     - 上下文特征（context feature）

（1）Label的分类

在Merlin中，Label有两种类别，分别是  
- **state align**（使用HTK来生成，以发音状态为单位的label文件，一个音素由几个发音状态组成）
- **phoneme align**（使用Festvox来生成，以音素为单位的label文件）

（2）txt to utt

文本到文本规范标注文件是非常重要的一步，这涉及自然语言处理，对于英文来说，具体工程实现可使用Festival，参见：[Creating .utt Files for English](http://www.cs.columbia.edu/~ecooper/tts/utt_eng.html)  
Festival 使用了英文词典，语言规范等文件，用最新的EHMM alignment工具将txt转换成包含了文本特征（如上下文，韵律等信息）的utt文件

（3）utt to label    

在获得utt的基础上，需要对每个音素的上下文信息，韵律信息进行更为细致的整理，对于英文的工程实现可参见：[Creating Label Files for Training Data](http://www.cs.columbia.edu/~ecooper/tts/labels.html)  

label文件的格式请参见：[lab_format.pdf](http://www.cs.columbia.edu/~ecooper/tts/lab_format.pdf)

（4）label to training-data（HMM模型聚类）TODO

由于基于上下文信息的HMM模型过于庞大，有必要对HMM模型进行聚类，即使用问题集Question file.（可以参考[决策树聚类](http://blog.csdn.net/quhediegooo/article/details/61202901)）（这个Question sets目测可以看HTS的文档来获得进一步的解释）

Question file 的解释：  
The questions in the question file will be used to convert the full-context labels into binary and/or numerical features for vectorization. It is suggested to do a manual selection of the questions, as the number of questions will affect the dimensionality of the vectorized input features.  

在Merlin目录下，merlin/misc/questions目录下，有两个不同的文件，分别是：  
questions-radio_dnn_416.hed        questions-unilex_dnn_600.hed  
查看这两个文件，我们不难发现，questions-radio_dnn_416.hed定义了一个416维度的向量，向量各个维度上的值由label文件来确定，也即是说，从label文件上提取必要的信息，我们可以很轻易的按照定义确定Merlin训练数据training-data；同理questions-unilex_dnn_600.hed确定了一个600维度的向量，各个维度上的值依旧是由label文件加以确定。

## 2 声码器Vocoder

Merlin中自带的vocoder工具有以下三类：Straight，World，World_v2  
这三类工具可以在Merlin的文件目录下找到，具体的路径如下merlin/misc/scripts/vocoder  
在介绍三类vocoder之前，首先说明几个概念：  

**MGC特征**：通过语音提取的MFCC特征由于维度太高，并不适合直接放到网络上进行训练，所以就出现了MGC特征，将提取到的MFCC特征降维（在这三个声码器中MFCC都被统一将低到60维），以这60维度的数据进行训练就形成了我们所说的MGC特征  
**BAP特征**： Band Aperiodicity的缩写  
LF0：LF0是语音的基频特征  

Straight  

音频文件通过Straight声码器产生的是：60维的MGC特征，25维的BAP特征，以及1维的LF0特征。  
通过 STRAIGHT 合成器提取的谱参数具有独特 特征(维数较高), 所以它不能直接用于 HTS 系统中, 需要使用 SPTK 工具将其特征参数降维, 转换为 HTS 训练中可用的 mgc(Mel-generalized cepstral)参数, 即, 就是由 STRAIGHT 频谱计算得到 mgc 频谱参数, 最后 利用原 STRAIGHT 合成器进行语音合成  

World  

音频文件通过World声码器产生的是：60维的MGC特征，可变维度的BAP特征以及1维的LF0特征，对于16kHz采样的音频信号，BAP的维度为1，对于48kHz采样的音频信号，BAP的维度为5  
网址为：[github.com/mmorise/World](https://github.com/mmorise/World)  


### mfcc vs mcep vs lsp
The vocoder extracts the parameters: spectral envelope, f0 contour, and aperiodicities. Then, you can transform them into MGCs (or MCEP), lf0, and bap, respectively.  
Do not confuse MGCs (or MCEP) with MFCCs, they are different features. The forced-alignment process uses MFCCs to recognize the phoneme structures of the data.  
论文”基于HMM的可训练中文语音合成“中提到：用于语音合成的参数 lsp 优于mcep，而mcep 优于mfcc  
可以参考这篇论文：[A Comparative Performance of Various Speech Analysis-Synthesis Techniques ](https://pdfs.semanticscholar.org/7301/b31571786b661b652b2ecbbcec570e00a18d.pdf)


## 3 训练模型——Duration和声学模型

语音合成和语音识别是一个相反的过程, 在语音 识别中, 给定的是一个 HMM 模型和观测序列(也就是 特征参数, 是从输入语音中提取得到), 要计算的是这 些观测序列对应的最有可能的音节序列, 然后根据语 法信息得到识别的文本. 而在合成系统中, 给定的是 HMM 模型和音节序列(经过文本分析得到的结果), 要 计算的是这些音节序列对应的观测序列, 也就是特征 参数.  

HTS的训练部分的作用就是由最初的原始语料库经过处理和模型训练后得到这些训练语料的HMM模型[5]。建模方式的选择首先是状态数的选择,因为语音的时序特性,一个模型的状态数量将影响每个状态持续的长短,一般根据基元确定。音素或半音节的基元,一般采用5状态的HMM;音节的基元一般采用10个状态。在实际的建模中,为了模型的简化,可以将HMM中的转移矩阵用一个时长模型(dur)替代,构成半隐马尔可夫模型HSMM hidden semi-Markov Model。用多空间概率分布对清浊音段进行联合建模,可以取得很好的效果。HTS的合成部分相当于训练部分的逆过程,作用在于由已经训练完成的HMM在输入文本的指导下生成参数,最终生成语音波形。具体的流程是:

 - 通过一定的语法规则、语言学的规律得到合成所需的上下文信息,标注在合成label中。
 - 待合成的label经过训练部分得到的决策树决策,得到语境最相近的叶结点HMM就是模型的决策。
 - 由决策出来的模型解算出合成的基频、频谱参数。根据时长的模型得到各个状态的帧数,由基频、频谱模型的均值和方差算出在相应状态的持续时长帧数内的各维参数数值,结合动态特征,最终解算出合成参数。
 - 由解算出的参数构建源-滤波器模型,合成语音。源的选取如上文所述:对于有基频段,用基频对应的单一频率脉冲序列作为激励;对于无基频段,用高斯白噪声作为激励

HSMM半隐马尔可夫模型的解释如下

A hidden semi-Markov model (HSMM) is a statistical model with the same structure as a [hidden Markov model](https://en.wikipedia.org/wiki/Hidden_Markov_model) except that the unobservable process is [semi-Markov](https://en.wikipedia.org/wiki/Semi-Markov_process) rather than [Markov](https://en.wikipedia.org/wiki/Markov_process). This means that the probability of there being a change in the hidden state depends on the amount of time that has elapsed since entry into the current state. This is in contrast to hidden Markov models where there is a constant probability of changing state given survival in the state up to that time

# 英文语音合成实现

Merlin自带英文语音合成，所以实现起来相对简单。你只需要训练Merlin自带的slt_arctic_full音频文件，安装FrontEnd，即可合成拥有基准效果的英文语音。

具体步骤如下参见：[Create_your_own_label_Using_Festival.md](https://github.com/Jackiexiao/merlin/blob/master/manual/Create_your_own_label_Using_Festival.md)

# 中文语音合成理论研究

0 汉语语言特点分析

汉语是单音节，声调语言。

**音节**

音节是由音素构成的。如啊”（ā）（1个音素），“地”（dì）（2个音素），“民”（mín）（3个音素）。  
音节示例：如“建设”是两个音节，“图书馆”是三个音节，“社会主义”是四个音节。汉语音节和汉字基本上是一对一，一个汉字也就是一个音节。  
音节包含了声母、韵母、音调三个部分。  
声母： 声母指音节开头的辅音，共有23个。如dā（搭）的声母是d  
韵母： 韵母指音节里声母后面的部分，共38。jiǎ（甲）的韵母是iǎ  
音节： 声调指整个音节的高低升降的变化。普通话里dū（督）、dú（毒）、dǔ（赌）、dù（度）  
根据《现代汉语词典》，汉语标准音节共 418 个  

**声调**

普通话的孤立音节有阴平、阳平、上声、去声和轻声五种音调

1 前端FrontEnd 

中文语音前端的主要步骤如下，详见论文：面向汉语统计参数语音合成的标注生成方法

![img](/img/image6.png)

中文label文件

可参考论文：面向汉语统计参数语音合成的标注生成方法 中提高的标注方法

中文label文件见：[chinese_label.md](https://github.com/Jackiexiao/merlin/blob/master/manual/chinese_label.md)

2 声码器Vocoder

声码器与语言种类无关，因而这里使用与英文相同的声码器。

# 中文语音合成实现

由于中文语音合成系统复杂，工作琐碎繁多，需要花费大量的时间，在有限的一个月时间里，学习语音合成的基础知识占据了大多数的时间，因此笔者在提交报告为止尚未实现中文语音合成，在这里简要谈谈我们已经完成的步骤以及后续所需要做的工作。

## 中文FrontEnd

考虑基于Festvox自行开发中文的FrontEnd，其中结合上述的中文语音合成理论研究以及网络上开源的中文文本分析器。这一步最为困难。

### (1) 中文词法分析工具包,请github 搜索 中文 自然语言处理,推荐使用第一个，其支持最为齐全
[HanLp](https://github.com/hankcs/HanLP)  
https://github.com/m00nlight/clj-bosonnlp  
Demo  
http://nlp.fudan.edu.cn/demo/  
http://thulac.thunlp.org/demo  
http://www.ltp-cloud.com/demo/  

# 附录

1 参考文献
范会敏, 何鑫. 中文语音合成系统的设计与实现[J]. 计算机系统应用, 2017(2):73-77.  
郝东亮, 杨鸿武, 张策,等. 面向汉语统计参数语音合成的标注生成方法[J]. 计算机工程与应用, 2016, 52(19):146-153.  
Merlin: An Open Source Neural Network Speech Synthesis System   
[英文](http://ssw9.net/papers/ssw9_PS2-13_Wu.pdf)
[中文](http://blog.csdn.net/lujian1989/article/details/56008786)

2 工程实现教程部分

 - [Getting started with the Merlin Speech Synthesis Toolkit](http://jrmeyer.github.io/merlin/2017/02/14/Installing-Merlin.html)  
 - [Merlin官方教程（正在建设中）](http://104.131.174.95/Merlin/dnn_tts/doc/build/html/)  
 - [**Columbia University TTS manual**](http://www.cs.columbia.edu/~ecooper/tts/)  
 - [HTS tutorial](http://hts.sp.nitech.ac.jp/?Tutorial)  
 - [Festvox教程（利用wav 和标记数据创造label）](http://festvox.org/bsv/)  
 - [speech.zone build-your-own-dnn-voice](http://www.speech.zone/exercises/build-your-own-dnn-voice/)   

3 相关软件

 - [Merlin语音合成系统 Github](https://github.com/CSTR-Edinburgh/merlin)
 - [Festvox](https://festvox.org)
 - [HTK](http://htk.eng.cam.ac.uk/) 
 - HTS
 - SPTK
 - World
 - Praat语音学软件

4 语音识别/合成基础知识

 - [机器学习&数据挖掘笔记_13（用htk完成简单的孤立词识别）](http://www.cnblogs.com/tornadomeet/p/3274078.htmli) 了解语音识别的基础
 - [上下文相关的GMM-HMM声学模型](http://www.cnblogs.com/cherrychenlee/p/6780460.html)
 - A beginners’ guide to statistical parametric speech synthesis[英文](http://www.cstr.ed.ac.uk/downloads/publications/2010/king_hmm_tutorial.pdf)[中文](https://shartoo.github.io/texttospeech/)
 - [语音产生原理与特征参数提取](http://blog.csdn.net/u010451580/article/details/51178190)
 - [台湾-语音信号处理教程（包含了语音合成教程）](http://www.mirlab.org/jang/books/audioSignalProcessing/)
 - [浅谈语音识别基础](http://www.jianshu.com/p/a0e01b682e8a)
 - [English tutorial for Chinese Spoken Language Processing](http://iscslp2016.org/slides.html)
 - [中文语音合成基本概念](http://staff.ustc.edu.cn/~zhling/Course_SSP/slides/Chapter_13.pdf)
 - [cmu_speech_slide](http://www.speech.cs.cmu.edu/15-492/slides/)

# 术语表

 - Front end 前端  
 - vocoder 声音合成机（声码器）  
 - MFCC 
 - 受限波尔曼兹机  
 - bap [band aperiodicity](http://blog.csdn.net/xmdxcsj/article/details/72420051)  
 - ASR：Automatic Speech Recognition自动语音识别  
 - AM：声学模型  
 - LM：语言模型  
 - HMM：Hiden Markov Model 输出序列用于描述语音的特征向量，状态序列表示相应的文字  
 - HTS：HMM-based Speech Synthesis System语音合成工具包  
 - HTK：Hidden Markov Model Toolkit 语音识别的工具包  
 - 自编码器  
 - SPTK：speech signal precessing toolkit  
 - SPSS : 统计参数语音合成statistical parametric speech synthesis  
 - pitch 音高：表示声音(基本)频率的高低
 - Timbre 音色
 - Zero Crossing Rate 过零率
 - Volume 音量
 - sil silence
 - syllable 音节
 - intonation 声调，语调，抑扬顿挫
 - POS part of speech
 - mgc 
 - mcep Mel-Generalized Cepstral Reprfesentation
 - mcc mel cepstral coefficents
 - mfcc Mel Frequency Cepstral Coefficents
 - LSP: Line Spectral Pair线谱对参数
 - monophone 单音素
 - biphone diphone 两音素
 - triphone 三音素
 - quadphone 四音素
 - 这里有[命名规则](http://wiki.c2.com/?NumericalPrefixes)
 - utterance 语音，发声
 - 英语韵律符号系统ToBI(Tone and Break Index)
 - CD-DNN-HMM（Context-Dependent DNN-HMM）
 - frontend :The part of a TTS system that transforms plain text into a linguistic representation is called a frontend
 - .wpa  word to phonetic alphabet
 - .cmp Composed acoustic features 
 - .scp system control program
 - .mlf master label file
 - .pam phonetic alphabets to model
 - .mgc mel generalized cepstral feature
 - .lf0 log f0 a representation of pitch（音高） 音高用基频表示
 - .mgc
 - .utt .utt files are the linguistic representation of the text that Festival outputs（full context training labels)
 - .cfg

# 联系作者
* Jackiexiao 微信:explorerrr
