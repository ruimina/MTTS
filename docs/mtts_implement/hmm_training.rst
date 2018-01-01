3.6 HMM训练
================

3.6.1 合成基元以及其状态数量的选择
-----------------------------------------

**如何选取合成基元**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

[3]对于汉语语音系统而言，常用的基本基元有音节、声韵母和音素。由于汉语有418个无调音节，如考虑语调则有1300多个音节，在进行上下文无关的建模时，选用音节作为基元可以取得比较好的性能。[todo 可以试一下使用音节来作为合成单元，看看合成效果]但如果考虑上下文相关的变化，则会由于基元数目太多而导致模型无法实现。而声韵母（声母21个，韵母todo个）与音素的数目都相对较少，因此可以用来作上下文相关模型的基元。

汉语大概有35个音素，但是音素并没有反映出汉语语音的特点，而且，相对于声韵母，音素显得十分不稳定，这就给标注带来了困难，进而影响声学建模，因此，音素也不适合作为上下文相关的合成基元。[3]

[todo]有没有用音节来做基元的，音素指的是？ming分成 m i n g四个音素？

这里选择音节和声韵母两种，为了模拟发音中的停顿，可以将短时停顿和长时停顿看做是合成基元，此外，将句子开始前和结束时的静音sil也当做合成基元

**合成基元的列表**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

声母 | 21个声母+wy+零声母(_A _E _I _O _U _V)
韵母 | 39个韵母
静音 | sil pau sp 

[contro] sil(silence) 表示句首和句尾的静音，pau(pause) 表示由逗号，顿号造成的停顿，句中其他的短停顿为sp(short pause)

[contro] 6个零声母（）的引入是为了减少上下文相关的tri-IF数目，这样就可以使得每个音节都是由声母和韵母组成，原先一些只有韵母音节可以被视作是声母和韵母的结构，这样一来，基元就只有 声母-韵母-声母 以及 韵母-声母-韵母 两种结构，而不会出现两个韵母相邻的情况，进而明显减少了上下文相关的基元。[3]

**基元状态数量的选择**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

一般我们选择将一个基元分成5个状态。假设每个状态都由一个高斯分布描述，那么总共的高斯分布数量等于上下文相关基元的数目*5，这样数量过多，在训练数据库不是足够大的情况下，很多基元会存在训练不充分的问题。解决的方法是采用参数共享的技术。例如进行状态共享（state Tying）建模，或者混合密度共享（Tied Mixture）建模

**上下文基元是否带声调**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

语音识别中，大多数系统使用的基元时不带有声调的。但在语音合成系统中，我们有两种选择：一是训练中仍采用无声调基元，然后在合成的最后阶段，根据汉语声调的模式调整基音周期，达到合成语调的目的。另一方法是，在训练中即使用带有声调的基元，然后在上下文相关训练时将它们进行状态共享，以降低模型规模，并提供近似合成未知基元的能力。[3]

[todo][contro]直觉上后者合成出来的语音可能更自然，本文选择后者（需要再进行测试评估）


3.6.2上下文相关的标注
-----------------------------------------

**设计上下文相关标注的规则**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

即要综合考虑有哪些上下文对当前音素发音的影响，总的来说，，需要考虑发音基元及其前后基元的信息，以及发音基元所在的音节、词、韵律词、韵律短语、语句相关的信息。[1]但是具体到哪些上下文是更有必要的就需要再仔细研究研究了[optimize]

**本文的上下文设计原则**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

对于以声韵母为合成基元来说，直观上使用使用相邻五音素的上下文相关信息要比3音素的要好。

**具体的上下文设计**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

本文将提供多种上下文设计以及对应的问题集，并探讨不同上下文设计对语音合成效果的影响[todo]

[3]也提供了一种上下文设计的思路


3.6.3 基于决策树的聚类
-----------------------------------------

[tmp]下面主要参考了[2]中的问题集设计

由于采用了大量的三音素结构，HMM模型数量骤增，过多的模型数量使得难以有足够的数据进行训练。决策树通过将模型进行归类很好地解决了这个问题。此外，实际语音合成时可能遇到训练数据中没有出现的基元，基于决策树（Decision Tree）的方法，可以使用那些可见基元的分布来合成在训练数据中不可见的基元。

决策树介绍TODO(可以抄写[2]中的介绍)

决策树的学习资料可以参见[todo]

### 3.6.4 问题集的设计
主要依据参考文献[3]


问题集(Question Set)即是决策树中条件判断的设计。问题集通常很大，由几百个判断条件组成，一个典型的问题集文件的部分内容如下:
TODO(Question Set 例子，可以找merlin的)

问题集的设计依赖于不同语言的语言学知识，对于中文语音合成而言，问题集的设计主要参考了以下的语言学知识：
* 声母特征划分，例如声母可以划分成塞音，擦音，鼻音，唇音等，具体参见[TODO]
* 韵母特征划分，例如韵母可以划分成单韵母，复合韵母，分别包含aeiouv的韵母，具体参见[TODO]

对于三音素模型而言，对于每个划分的特征，都会产生3个判断条件，该音素是否满足条件，它的左音素和右音素是否满足条件。例如
* 判断当前，前接，后接音素/单元是否为擦音
* QS 'C_Fricative'
* QS 'L_Fricative'
* QS 'R_Fricative'
 

参考微软论文:HMM-based Mandarin Singing Voice Synthesis Using Tailored Synthesis Units and Question Sets

**Question Set for Decision Trees**
Based on unit definition and contextual factors, we define five categories for the questions in the question set. The five categories of the question set are sub-syllable, syllable, phrase, song, and note. The details of the question set are described as follows.
1. Sub-syllable: (current sub-syllable, preceding one and two sub-syllables, and succeeding one and two sub-syllables) Initial/final, final with medial, long model, articulation category of the initial, and pronunciation category of the final
2. Syllable: The number of sub-syllables in a syllable and the position of the syllable in the note
3. Phrase: The number of sub-syllables/syllables in a phrase
4. Song: Average number of sub-syllables/syllables in each measure of the song and the number of phrases in this song
5. Note: The absolute/relative pitch of the note; the key, beat, and tempo of the note; the length of the note by syllable/0.1 second/thirty-second note; the position of the current note in the current measure by syllable/0.1 second/ thirty-second note; and the position of the current note in the current phrase syllable/0.1 second/thirty-second note 

### 3.6.5 决策树的构建
### 3.6.6 HMM拓扑结构以及声学参数结构

**基元状态的拓扑结构**
本文选择了从左至右无跳转的HMM拓扑结构，其他结构详见[3]3.1.2节  

(begin) 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (end) 

表示可以跳转到自身的状态，1和7分别是起始和结束状态。

**声学参数的结构**
TODO，可参考[3]

3.6.6 状态时长模型
-----------------------------------------

3.6.7 基音周期模型
-----------------------------------------