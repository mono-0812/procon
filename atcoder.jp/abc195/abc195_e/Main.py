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
#　　　　　V
#　　 ／￣ψ￣＼
#　　| 合格祈願 |
#　　|＿＿＿＿＿|
##############################################################################
N=II();S=I();X=I()
dp=[[False]*7 for _ in range(N+1)]
dp[-1][0]=True
for i in range(N-1,-1,-1):
    s=int(S[i])
    x=X[i]
    for d in range(7):
        if x=="A":
            dp[i][d]=dp[i+1][(10*d+s)%7] & dp[i+1][(10*d)%7]
        if x=="T":
            dp[i][d]=dp[i+1][(10*d+s)%7] | dp[i+1][(10*d)%7]
print("Takahashi" if dp[0][0] else "Aoki")