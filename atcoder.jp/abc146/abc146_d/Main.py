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
import sys
sys.setrecursionlimit(2000000)
n=II()
li=[[] for i in range(n)]
for i in range(n-1):
    a,b=IIS()
    li[a-1].append((b-1,i))
ans=[-1]*(n-1)
def dfs(v,color,parent):
    c=1
    for i in range(len(li[v])):
        u=li[v][i][0];d=li[v][i][1]
        if u==parent:continue
        if c==color:c+=1
        ans[d]=c;c+=1
        dfs(u,ans[d],v)
    return
dfs(0,-1,-1)
mx=0
for i in ans:
    mx=max(i,mx)
print(mx)
print(*ans)
         
         