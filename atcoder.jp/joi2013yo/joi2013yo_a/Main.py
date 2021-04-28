import bisect,collections,copy,heapq,itertools,math,string,sys,queue,datetime,time
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
l=II()
a=II()
b=II()
c=II()
d=II()
print(l-max(math.ceil(a/c),math.ceil(b/d)))