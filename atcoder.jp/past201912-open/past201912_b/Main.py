import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
now=II()
for i in range(n-1):
    val=II()
    if val-now>0:
        print("up",val-now)
    elif now-val>0:
        print("down",now-val)
    else:
        print("stay")
    now=val
