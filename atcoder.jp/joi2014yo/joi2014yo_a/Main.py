import bisect,collections,copy,heapq,itertools,math,string,sys,queue,datetime,time
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
sm=0
for i in range(5):
    sm+=max(40,II())
print(sm//5)