# encoding: utf-8
# leetcode3.py

import os
import time


# encoding: utf-8
# lswrc.py


import os


def noRepeatString(s):
    s_dict = {}
    for item in s:
        if s_dict.has_key(item):
            return False
        else:
            s_dict[item] = 0
    return True


def lengthOfLongestSubstring(s):
    len_s = len(s)
    max = 0
    s_dict = {}
    begin = 0
    for index, item in enumerate(s):
        if s_dict.has_key(item):
            l = len(s_dict)
            if max < l:
                max = l
            begin_tmp = s_dict[item] + 1
            for i in range(begin, s_dict[item] + 1):
                del s_dict[s[i]]
            begin = begin_tmp
        s_dict[item] = index
    l = len(s_dict)
    if max < l:
        max = l
    return max


start = time.clock()
print "start at", start
s = open("data.txt").read()
print "the length of the string is ", len(s)
length = lengthOfLongestSubstring(s)
print "the length Of Longest Substring is ", length

end = time.clock()
print "end at", end
print "the duration :", end - start, "second"