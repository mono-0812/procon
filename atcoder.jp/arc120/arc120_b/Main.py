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
h,w=IIS()
S=[I() for i in range(h)]
li=[-1 for i in range(1010)]
#B 2 R 1 . 0
for i in range(h):
    for j in range(w):
        if S[i][j]=="B":
            if li[i+j]==1:
                print(0)
                exit()
            else:
                li[i+j]=2
        if S[i][j]=="R":
            if li[i+j]==2:
                print(0)
                exit()
            else:
                li[i+j]=1
        else:
            if li[i+j]==-1:
                li[i+j]=0
mod=998244353
ans=1
for i in li:
    if i==0:
        ans=(ans*2)%mod
print(ans%mod)
                