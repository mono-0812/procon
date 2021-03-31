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
li=[]
for i in range(5):
    li.append(II())
k=II()
for i in range(5):
    for j in range(5):
        if abs(li[i]-li[j])>k:
            print(":(")
            exit()
print("Yay!")