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
f=[]
for i in range(h):
    l=list("".join(I()))
    if l!=["."]*w:
        f.append(l)
st=set()
for j in range(w):
    L=[]
    for i in range(len(f)):
        L.append(f[i][j])
    if L==["."]*(len(f)):
        st.add(j)
for i in range(len(f)):
    ans=""
    for j in range(w):
        if not j in st:
            ans+=f[i][j]
    print(ans)
        

    
