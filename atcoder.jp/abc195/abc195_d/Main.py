import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
############################################
n,m,q=IIS()
items=[]
for _ in range(n):
    w,v=IIS()
    items.append((v,w))
X=LIIS()
items.sort(reverse=True)
for _ in range(q):
    L,R=IIS()
    lis=sorted(X[:L-1]+X[R:])+[INF]
    val=0
    for v,w in items:
        pos=bisect.bisect_left(lis,w)
        if pos < len(lis)-1:
            val+=v
            lis.pop(pos)
    print(val)