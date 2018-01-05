3.5 语音学处理
===========================================

[2]文使用的声学参数为：24阶梅尔倒谱参数，一阶能量以及一阶基频参数，共78维参数；

3.5.1 声学建模参数的选取
-----------------------------------------------------------------------

相比其他声学建模参数，例如线性预测倒谱参数LPCC，其缺点在于对辅音的描述能力较差，抗噪声性能较差；而由于STRAIGHT参数建模算法不够成熟，因而合成系统稳定性较差；而MFCC参数能够反映人耳的听觉特性，而且它的提取算法成熟，合成音质较高，计算复杂度低，能够实现实时合成等。[4]

可以使用HTK工具提取MFCC谱参数和基频F0


**mfcc vs mcep vs lsp**

The vocoder extracts the parameters: spectral envelope, f0 contour, and aperiodicities. Then, you can transform them into MGCs (or MCEP), lf0, and bap, respectively.  

Do not confuse MGCs (or MCEP) with MFCCs, they are different features. The forced-alignment process uses MFCCs to recognize the phoneme structures of the data.  

论文”基于HMM的可训练中文语音合成“中提到：用于语音合成的参数 lsp 优于mcep，而mcep 优于mfcc  

可以参考这篇论文：`A Comparative Performance of Various Speech Analysis-Synthesis Techniques <https://pdfs.semanticscholar.org/7301/b31571786b661b652b2ecbbcec570e00a18d.pdf>`_


3.5.2 HTK提取MFCC谱参数和基频F0
----------------------------------------------------------------------------

可见文献[4]