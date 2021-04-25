import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()
B=LIIS()
mi=0
mx=INF
for i in A:
    mi=max(mi,i)
for i in B:
    mx=min(mx,i)
print(max(mx-mi+1,0))