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
x=II()
ans=1
for i in range(2,x+1):
    val=i
    while val<=x:
        val*=i
        if val<=x:
            ans=max(ans,val)
print(ans)