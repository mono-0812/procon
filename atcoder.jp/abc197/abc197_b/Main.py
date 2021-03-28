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
h,w,x,y=IIS()
li=[]
ans=0
for i in range(h):
    li.append(I())
    if i==x-1:
        for j in reversed(li[i][:y-1]):
            if not j=="#":
                ans+=1
            else:
                break
        for j in li[i][y:]:
            if not j=="#":
                ans+=1
            else:
                break
for i in range(x-1,-1,-1):
    if not li[i][y-1]=="#":
        ans+=1
    else:
        break
for i in range(x,h):
    if not li[i][y-1]=="#":
        ans+=1
    else:
        break
print(ans)


    