import bisect,collections,copy,heapq,itertools,math,string,sys,queue
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
##############################################################################
n=II()
left_most=[INF]*(n+1)
right_most=[-INF]*(n+1)
colors=[]
for i in range(n):
    x,c=IIS()
    colors.append(c)
    left_most[c]=min(left_most[c],x)
    right_most[c]=max(right_most[c],x)
colors=list(set(colors))
colors.sort()
l,r,lpos,rpos=0,0,0,0
for c in colors:
    nlpos,nrpos=left_most[c],right_most[c]
    nl=min(l+abs(lpos-nrpos)+abs(nrpos-nlpos),
    r+abs(rpos-nrpos)+abs(nrpos-nlpos))
    nr=min(l+abs(lpos-nlpos)+abs(nrpos-nlpos),
    r+abs(rpos-nlpos)+abs(nrpos-nlpos))
    lpos,rpos,l,r=nlpos,nrpos,nl,nr
ans=min(l+abs(lpos),r+abs(rpos))
print(ans)