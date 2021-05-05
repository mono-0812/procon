import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=10**9+7
##############################################################################
n=II()
sc=collections.Counter(I())
ans=1
for i in sc:
    ans=(ans*(sc[i]+1))%MOD
print(ans-1)