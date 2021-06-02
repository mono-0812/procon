import collections
import itertools
import math
import decimal
import bisect
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
a,b,c=IIS()
if a==b:
    print(c)
elif b==c:
    print(a)
elif a==c:
    print(b)
else:
    print(0)