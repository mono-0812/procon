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
h,w,a,b=IIS()
ans=[[0]*w for i in range(h)]
for i in range(a,w):
    for j in range(b,h):
        ans[j][i]=1
for i in range(a):
    for j in range(b):
        ans[j][i]=1
[print("".join(map(str,ans[i]))) for i in range(h)]
