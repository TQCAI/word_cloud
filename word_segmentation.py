#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
import jieba

with open("processed.txt", "r", encoding="utf-8") as f:
    txt = f.read()

try:
    import pkuseg

    seg = pkuseg.pkuseg()
    words = seg.cut(txt)
except Exception as e:
    print(e)
    words = jieba.cut(txt)
res = []
for word in words:
    if len(word) > 1:
        res.append(word)
with open("words.txt", "w+", encoding="utf-8") as f:
    f.write("\n".join(res))
