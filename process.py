#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
import re
import pandas as pd
from zhon.hanzi import punctuation


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def format_str(content):
    res = ""
    for c in content:
        if ord(u'\u4e00') <= ord(c) <= ord(u'\u9fa5'):
            res += c
    return res


df = pd.read_csv("comments.csv")
final_str = ""
for comment in df.comments:
    processed = re.sub(f"[{punctuation}]", "", comment)
    processed = format_str(processed)
    final_str += processed
with open("processed.txt", "w+", encoding="utf-8") as f:
    f.write(final_str)
