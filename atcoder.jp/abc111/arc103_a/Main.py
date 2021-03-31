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
V=LIIS()
li=[]
key=0
for i in range(0,n,2):
    li.append(V[i])
ls=collections.Counter(li)
vals=[]
for i in ls.keys():
    vals.append((ls[i],i))
li2=[]
val2=0
for i in range(1,n,2):
    li2.append(V[i])
ls2=collections.Counter(li2)
vals2=[]
for i in ls2.keys():
    vals2.append((ls2[i],i))
vals.sort(reverse=True,key=lambda x: x[0])
vals2.sort(reverse=True,key=lambda x: x[0])
ans=-1
for i in range(min(len(vals),2)):
    for j in range(min(len(vals2),2)):
        if vals[i][1]==vals2[j][1]:continue
        ans=max(ans,vals[i][0]+vals2[j][0])
if ans==-1:
    ans=n//2
print(n-ans)
