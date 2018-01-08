# 问题集设计规则

问题集的设计依赖于不同语言的语言学知识，而且与上下文标注文件相匹配，改变上下文标注方法也需要相应地改变问题集，对于中文语音合成而言，问题集的设计的规则有:
* 前前个，前个，当前，下个，下下个声韵母分别是某个合成基元吗，合成基元共有65个，例如判断是否是元音a QS "LL-a" QS "L-a" QS "C-a" QS "R-a" QS "RR-a"
* 声母特征划分，例如声母可以划分成塞音，擦音，鼻音，唇音等，声母特征划分24个
* 韵母特征划分，例如韵母可以划分成单韵母，复合韵母，分别包含aeiouv的韵母，韵母特征划分8个
* 其他信息划分，词性划分，26个词性; 声调类型，5个; 是否是声母或者韵母或者静音，3个
* 韵律特征划分，如是否是重音，重音和韵律词/短语的位置数量
* 位置和数量特征划分

### 声母的划分特征

划分特征  | 描述    | 基元列表
-------- | ------- | -------
Stop|塞音|b, d, g, p, t, k
Aspirated Stop|塞送气音|b，d，g
Unaspirated Stop|非塞送气音|P，t,k
Affricate|塞檫音|z，zh，j，c，ch，q
Aspirated Affricate|塞擦送气音|z，zh，j
Unaspirated Affricate|非塞檫送气音|c，ch，q
Fricative|擦音|f，s，sh，x, h，r
Fricative2|擦音2|f，s, sh，x，h，r，k
Voiceless Fricative|清檫音|f，s，sh，x，h
Voice Fricative|浊擦音|r，k
Nasal|鼻音|m, n
Nasal2|鼻音2|m, n, l
Labial|唇音|b，p，m
Labial2|唇音2|b，p，m，f
Apical|顶音|z，c，s，d，t，n，l，zh，ch，sh，r
Apical Front|顶前音|z，c，s
Apical 1|顶音1|d，t，n，l
Apical2|顶音2|d，t
Apical3|顶音3|n，l
Apical End|顶后音1|zh，ch，sh，r
Apical End2|顶后音2|zh，ch, sh
Tongue Top|舌前音|j，q，x
Tongue Root|舌根音|g, k，h
Zero|零声母|y w
XFuyin|全部声母（包含零声母）|略
Fuyin|全部声母（不包含零声母）|略

### 韵母的划分特征[contro：文献3中的划分有点奇怪]

划分特征|描述|基元列表
-------- | ------- | -------
Single Yun|单韵母|a，i，u，e, ee, o，v, ic，ih
Com Yun|复合韵母|an，ai，ang....vn
Type A|含有a的韵母|a, ia, an, ang, ai, ua, ao
Type E|含有e的韵母|e，ie，ve，ei, uei
Type I|含有I的韵母|i，ai，ei，uei, ia, ian, iang，iao， ie, in, ing, iong, iou
Type O|含0的韵母|o, ao, uo, ou, ong, iou
Type U|含u的韵母|u, ua, uen, ueng, uo, iou
Type V|含V的韵母|v，vn, ve

### 位置数量，韵律特征问题

主要参见上下文相关标注进行对应的问题集设计

标号  |  含义
---- | ----
b1  |  当前音节/字到语句开始字的距离
b2  |  当前音节/字到语句结束字的距离
b3  |  当前音节/字在词中的位置（正序）
b4  |  当前音节/字在词中的位置（倒序）
b5  |  当前音节/字在韵律词中的位置（正序）
b6  |  当前音节/字在韵律词中的位置（倒序）
b7  |  当前音节/字在韵律短语中的位置（正序）
b8  |  当前音节/字在韵律短语中的位置（倒序）
---- | ----
c1  |  前一个词的词性
c2  |  当前词的词性
c3  |  后一个词的词性
c4  |  前一个词的音节数目
c5  |  当前词中的音节数目
c6  |  后一个词的音节数目
c7  |  当前词在韵律词中的位置（正序）
c8  |  当前词在韵律词中的位置（倒序）
---- | ----
d1  |  前一个韵律词的音节数目
d2  |  当前韵律词的音节数目
d3  |  后一个韵律词的音节数目
d4  |  前一个韵律词的词数目
d5  |  当前韵律词的词数目
d6  |  后一个韵律词的词数目
d7  |  当前韵律词在韵律短语的位置（正序）
d8  |  当前韵律词在韵律短语的位置（倒序）
---- | ----
e1  |  前一韵律短语的音节数目
e2  |  当前韵律短语的音节数目
e3  |  后一韵律短语的音节数目
e4  |  前一韵律短语的词数目
e5  |  当前韵律短语的词数目
e6  |  后一韵律短语的词数目
e7  |  前一韵律短语的韵律词个数
e8  |  当前韵律短语的韵律词个数
e9  |  后一韵律短语的韵律词个数
e10  |  前一韵律短语的语调类型
e11  |  当前韵律短语的语调类型
e12  |  后一韵律短语的语调类型
e13  |  当前韵律短语在语句中的位置（正序）
e14  |  当前韵律短语在语句中的位置（倒序）
---- | ----
g1  |  语句的语调类型
g2  |  语句的音节数目
g3  |  语句的词数目
g4  |  语句的韵律词数目
g5  |  语句的韵律短语数目



### 重音

如果考虑重音，下面关于重音的示例问题，可以参照 `HTS label <http://www.cs.columbia.edu/~ecooper/tts/lab_format.pdf>`_ 以及 `Merlin Questions <https://github.com/CSTR-Edinburgh/merlin/tree/master/misc/questions>`_ 设计相关的数量，位置问题

例如
* 前后、当下基元是否是重音
* 韵律短语中，当前音节前面的重音有多少个
* 重音的位置
