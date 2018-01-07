### 问题集示例

Question          | 含义
----------------- | -------------------
QS "C_a"        |当前单元是否为韵母a
QS "L_Fricative"|前接单元是否为擦音
QS "R_Fricative"|后接单兀是否为擦音
QS "C_Fricative"|当前单元是否为擦音
QS "C_Stop"|当前单元是否为塞音
QS "C_Nasal"|当前单元是否为鼻音
QS "C_Labial"|当前单元是否为唇音
QS "C_Apieal"|当前单元是否为顶音
QS "C_TypeA"|含有a的韵母
QS "C_TypeE"|含有e的韵母
QS "C_TypeI"|含有i的韵母
QS "C_POS==a"|当前单元是否为形容词
QS "C_Toner==1"|当前单元音调是否为一声


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
Single Yun|单韵母|a，i，u，e，o，v, ic，ih
Com Yun|复合韵母|an，ai，ang....vn
Type A|含有a的韵母|a, ia, an, ang, ai, ua, ao
Type E|含有e的韵母|e，ie，ve，ei, uei
Type I|含有I的韵母|i，ai，ei，uei, ia, ian, iang，iao， ie, in, ing, iong, iou
Type O|含0的韵母|o, ao, uo, ou, ong, iou
Type U|含u的韵母|u, ua, uen, ueng, uo, iou
Type V|含V的韵母|v，vn, ve

QS "C-Stop"
QS "C-Aspirated_Stop"
QS "C-Unaspirated_Stop"
QS "C-Affricate"
QS "C-Aspirated_Affricate"
QS "C-Unaspirated_Affricate"
QS "C-Fricative"
QS "C-Fricative2"
QS "C-Voiceless_Fricative"
QS "C-Voice_Fricative"
QS "C-Nasal"
QS "C-Nasal2"
QS "C-Labial"
QS "C-Labial2"
QS "C-Apical"
QS "C-Apical_Front"
QS "C-Apical1"
QS "C-Apical2"
QS "C-Apical3"
QS "C-Apical_End"
QS "C-Apical_End2"
QS "C-Tongue_Top"
QS "C-Tongue_Root"
QS "C-Zero"
QS "C-XFuyin"
QS "C-Fuyin"


### 判断是否是声母，韵母，精音(sil+pau+sp)
QS "C-initial"
QS "C-final"
QS "C-silence"

### 声调
QS "C-Toner==1"         {}
QS "C-Toner==2"         {}
QS "C-Toner==3"         {}
QS "C-Toner==4"         {}
QS "C-Toner==5"         {}

QS "C-TypeA"

### 词性部分
QS "C-POS==a"
QS "C-POS==b"
QS "C-POS==c"
QS "C-POS==d"
QS "C-POS==e"
QS "C-POS==f"
QS "C-POS==g"
QS "C-POS==h"
QS "C-POS==i"
QS "C-POS==j"
QS "C-POS==k"
QS "C-POS==l"
QS "C-POS==m"
QS "C-POS==n"
QS "C-POS==o"
QS "C-POS==p"
QS "C-POS==q"
QS "C-POS==r"
QS "C-POS==s"
QS "C-POS==t"
QS "C-POS==u"
QS "C-POS==v"
QS "C-POS==w"
QS "C-POS==x"
QS "C-POS==y"
QS "C-POS==z"


### 合成基元部分
QS "C-b"
QS "C-p"
QS "C-m"
QS "C-f"
QS "C-d"
QS "C-t"
QS "C-n"
QS "C-l"
QS "C-g"
QS "C-k"
QS "C-h"
QS "C-j"
QS "C-q"
QS "C-x"
QS "C-zh"
QS "C-ch"
QS "C-sh"
QS "C-r"
QS "C-z"
QS "C-c"
QS "C-s"
QS "C-y"
QS "C-w"
QS "C-a"
QS "C-o"
QS "C-e"
QS "C-i"
QS "C-u"
QS "C-v"
QS "C-ic"
QS "C-ih"
QS "C-er"
QS "C-ai"
QS "C-ei"
QS "C-ao"
QS "C-ou"
QS "C-ia"
QS "C-ie"
QS "C-ua"
QS "C-uo"
QS "C-ve"
QS "C-iao"
QS "C-iou"
QS "C-uai"
QS "C-uei"
QS "C-an"
QS "C-ian"
QS "C-uan"
QS "C-van"
QS "C-en"
QS "C-in"
QS "C-uen"
QS "C-vn"
QS "C-ang"
QS "C-iang"
QS "C-uang"
QS "C-eng"
QS "C-ing"
QS "C-ueng"
QS "C-ong"
QS "C-iong"
QS "C-sil"
QS "C-sp"
QS "C-pau"