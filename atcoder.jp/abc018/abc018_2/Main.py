import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
s=I()
n=II()
for _ in range(n):
    l,r=IIS()
    s=s[:l-1]+s[l-1:r][::-1]+s[r:]
print(s)