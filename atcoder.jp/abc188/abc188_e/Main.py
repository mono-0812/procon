import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=10**9+7
sys.setrecursionlimit(10**8)
##############################################################################
n,m=IIS()
A=LIIS()
edge=[[] for i in range(n)]
for i in range(m):
    x,y=IIS()
    edge[y-1].append(x-1)
dp=[0]*n
ans=-10**10
for i in reversed(range(n)):
    if dp[i]!=0:
        ans=max(ans,dp[i]-A[i])
    for j in edge[i]:
        dp[j]=max(A[i],dp[i],dp[j])
print(ans)