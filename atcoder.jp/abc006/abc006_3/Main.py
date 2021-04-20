import bisect,collections,copy,heapq,itertools,math,string,sys,random
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
import decimal
##############################################################################
n,m=IIS()
for y in range(n+1):
    if ((m-2*n-y)/2).is_integer() and (n-y-((m-2*n-y)/2)).is_integer():
        if (n-y-((m-2*n-y)//2))>=0 and y>=0 and ((m-2*n-y)//2)>=0:
            print((n-y-((m-2*n-y)//2)),y,((m-2*n-y)//2))
            exit()
print(-1,-1,-1)
