import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=998244353
import decimal
##############################################################################
n,k=IIS()
print(decimal.Decimal((((k-1)*(n-k))*6+3*(n-1)+1))/decimal.Decimal(n**3))