import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
A=LIIS()
cnt=0
ans=0
for i in range(n):
    if A[i]<=A[i]*-1:
        cnt+=1
        A[i]=A[i]*-1
    ans+=max(A[i],A[i]*-1)
A.sort()
if cnt%2:
    ans+=(A[0]*-1)*2
print(ans)

