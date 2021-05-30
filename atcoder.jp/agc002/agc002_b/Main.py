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
n,m=IIS()
li=[1 for i in range(n)]
li2=[0 for i in range(n)]
li2[0]=1
ans=1
v=set([1])
for i in range(m):
    x,y=IIS()
    if x in v:
        if li[x-1]>=2:
            li2[y-1]=1
        else:
            v.remove(x)
            li2[y-1]=1
            li2[x-1]=0
        v.add(y)
    li[x-1]-=1
    li[y-1]+=1
print(sum(li2))