import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=998244353
##############################################################################
n=II()
A=LIIS()
B=LIIS()
ans=0
mxa=0
for i in range(n):
    mxa=max(mxa,A[i])
    ans=max(ans,mxa*B[i])
    print(ans)