import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
a,b,c=IIS()
if a**2+b**2<c**2:
    print("Yes")
else:
    print("No")