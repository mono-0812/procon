import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,a,b=IIS()
if (b-a)%2:
    print("Borys")
else:
    print("Alice")

