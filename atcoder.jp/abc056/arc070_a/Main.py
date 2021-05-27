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
#(n+1)*n//2
x=II()
l=0
r=10**9+10
while r-l>1:
    mid=(l+r)//2
    if (mid+1)*mid//2>=x:
        r=mid
    else:
        l=mid
print(r)