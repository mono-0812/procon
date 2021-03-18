import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
X=LIIS()
SX=sorted(X)
v1=SX[n//2-1]
v2=SX[n//2]
for i in range(n):
    if X[i]<=v1:
        print(v2)
    elif X[i]>=v2:
        print(v1)

