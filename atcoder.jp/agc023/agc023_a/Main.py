import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
A=collections.Counter(itertools.accumulate(LIIS()))
ans=0
for i in A.keys():
    if i==0:
        ans+=A[i]
    ans+=A[i]*(A[i]-1)//2
print(ans)
