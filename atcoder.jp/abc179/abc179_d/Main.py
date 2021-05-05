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
n,k=IIS()
R,L=[],[]
dp=[0]*(n+1)
dp[1]=1
dpsum=[0]*(n+1)
dpsum[1]=1
for i in range(k):
    l,r=IIS()
    L.append(l)
    R.append(r)
for i in range(1,n+1):
    for j in range(k):
        l,r=i-R[j],i-L[j]
        if r<=0:continue
        l=max(1,l)
        dp[i]=(dp[i]+dpsum[r]-dpsum[l-1])%MOD
    dpsum[i]=(dpsum[i-1]+dp[i])%MOD
print(dp[n])
