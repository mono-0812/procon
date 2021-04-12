import bisect,collections,copy,heapq,itertools,math,string,sys,queue
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
li=[]
for i in range(n):li.append(II())
li.sort()
sm=sum(li)
f=True
if sm%10:
    print(sm);exit()
for i in range(n):
    if (sm-li[i])%10==0:
        continue
    else:
        sm-=li[i]
        f=False
        break
if f:print(0)
else:print(sm)

