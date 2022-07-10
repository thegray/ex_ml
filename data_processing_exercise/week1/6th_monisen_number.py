# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 11:20:07 2018

@author: Bangun
"""

def primaltest(bil): #from wikipedia :)
    if bil <= 1:
        return False
    elif bil <= 3:
        return True
    elif bil % 2 == 0 or bil % 3 == 0:
        return False
    i = 5
    while i * i <= bil:
        if bil % i == 0 or bil % (i + 2) == 0:
            return False
        i = i + 6
    return True

if __name__ == '__main__':
    n = 1
    m = 0
    p = 1
    while n < 7:
        if primaltest(p):
            m = (2 ** p) - 1
            if primaltest(m):
                print("m: {}\nn-th: {}\np: {}\n----".format(m,n,p))
                n += 1
        p += 1
