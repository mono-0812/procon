import bisect,collections,copy,heapq,itertools,math,string,sys,queue,datetime,time
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=INF
a=INF
for i in range(3):
    n=min(II(),n)
for i in range(2):
    a=min(II(),a)
print(a+n-50)