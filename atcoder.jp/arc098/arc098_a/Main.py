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
n=II();s=I()
w=[0]*n
e=[0]*n
ans=INF
for i in range(n):
    w[i]=w[i-1]
    if s[i]=="W":
        w[i]+=1
for i in range(n):
    if i==0:
        if s[n-i-1]=="E":
            e[n-i-1]+=1
        continue
    e[n-i-1]=e[n-i]
    if s[n-i-1]=="E":
        e[n-i-1]+=1
for i in range(n):
    if i>0:
        val=w[i-1]
    else:
        val=0
    if i+1<n:
        val2=e[i+1]
    else:
        val2=0
    ans=min(val+val2,ans)
print(ans)