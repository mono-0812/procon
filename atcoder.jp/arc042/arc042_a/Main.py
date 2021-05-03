import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,m=IIS()
li=list(reversed(range(1,n+1)))
for i in range(m):
    k=II()
    li.append(k)
path=[False for i in range(n)]
for i in reversed(li):
    if path[i-1]:continue
    path[i-1]=True
    print(i)