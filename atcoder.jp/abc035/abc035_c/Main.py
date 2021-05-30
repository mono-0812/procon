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
n,q=IIS()
li=[0 for i in range(n)]
for i in range(q):
    l,r=IIS()
    li[l-1]+=1
    if r<n:
        li[r]+=-1
v=0
for i in range(n):
    v+=li[i]
    if v%2:
        li[i]=1
    else:
        li[i]=0
print("".join([str(li[i]) for i in range(n)]))