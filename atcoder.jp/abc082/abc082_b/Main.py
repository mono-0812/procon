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
s=list(I())
t=list(I())
s.sort()
t.sort(reverse=True)
s="".join(s)
t="".join(t)
if s<t:
    print("Yes")
else:
    print("No")

