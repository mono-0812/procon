import collections
import itertools
import math
import decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
t=II()
for i in range(t):
    n=II()
    s1=I()
    s2=I()
    s3=I()
    print(n*"0"+n*"1"+"0")