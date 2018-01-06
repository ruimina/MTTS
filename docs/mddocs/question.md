### 问题集示例

Question          | 含义
----------------- | -------------------
QS ’L_Fricative’|前接单元是否为擦音
QS ’R_Fricative’|后接单兀是否为擦音
QS ’C_Fricative’|当前单元是否为擦音
QS 'C_Stop'|当前单元是否为塞音
QS 'C_Nasal|当前单元是否为鼻音
QS ,C_Labial,|当前单元是否为唇音
QS 'C_Apieal’|当前单元是否为顶音
QS ,C_TypeA'|含有a的韵母
QS 'C_TypeE'|含有e的韵母
QS 'C_TypeI|含有i的韵母
QS ,C_POS==a,|当前单元是否为形容词
QS ’C_POS==Real’|当前单元是否为实词
QS ,C_Toner==1,|当前单元音调是否为一声



### 完整的问题集[todo]
具体的设计可以参考merlin的问题集同时需要考虑到使用的上下文标注
QS "C_Toner==1"         {}
QS "C_Toner==2"         {}
QS "C_Toner==3"         {}
QS "C_Toner==4"         {}
QS "C_Toner==5"         {}