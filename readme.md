# 汉语自动分词

## 环境
* python 3.7

##  数据
* dict_ch.txt：ce(ms-word).txt 经过预处理后的中文词典文件。

## 基于词典的汉语自动分词算法
* 创建中文词典 dict_ch。
* 用户输入中文句子 S。
* 使用基于dict_ch 的正向最大匹配算法对 S 进行分词，得到分词后的列表 tokens_fmm。
* 使用基于dict_ch 的反向最大匹配算法对 S 进行分词，得到分词后的列表 tokens_bmm。
* 如果tokens_fmm 和 tokens_bmm 相同，则饭回 tokens_fmm。
* 如果不一样，则返回分词个数小的列表。
* 如果分词个数相同，但分词列表不同，则返回分词列表中含有单字更少的列表。
* 如果含有的单字个数也相同，则返回 tokens_bmm。