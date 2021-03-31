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
h,w=IIS()
n=II()
A=LIIS()
ans=[[0]*w for _ in range(h)]
c=0
for i in range(h):
    for j in range(w):
        if i%2==0:
            ans[i][j]=c+1
        else:
            ans[i][w-j-1]=c+1
        A[c]-=1
        if A[c]<=0:
            c+=1
for i in ans:
    print(*i)
