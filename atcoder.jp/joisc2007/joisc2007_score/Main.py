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
n=II()
li=[]
for i in range(n):li.append(II())
scores=sorted(li,reverse=True)
dic={}
val=0
for i in range(n):
    if dic.get(scores[i]):val+=1;continue
    dic[scores[i]]=i+1
for i in li:
    print(dic[i])