import bisect,collections,copy,heapq,itertools,math,string,sys,queue,datetime,time
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
for i in range(9):
    n-=II()
print(n)