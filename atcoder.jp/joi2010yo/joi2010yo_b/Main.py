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
n,m=IIS()
f=[];s=[]
for i in range(n):
    f.append(II())
for i in range(m):
    s.append(II())
pos=1
ans=0
for i in range(m):
    ans+=1
    pos+=s[i]
    if pos>=n:break
    pos+=f[pos-1]
    if pos>=n:break
print(ans)
