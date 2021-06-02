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
n,k=IIS()
ans=0
for i in range(1,n+1):
    for j in range(1,k+1):
        ans+=int(str(i)+"0"+str(j))
print(ans)