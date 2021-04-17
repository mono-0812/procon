import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,p=IIS()
A=LIIS()
dp=[[0]*2 for i in range(n)]
dp[0][0]=1
dp[0][A[0]%2]+=1
for i in range(1,n):
    if A[i]%2==1:
        dp[i][0]+=dp[i-1][0]+dp[i-1][1]
        dp[i][1]+=dp[i-1][0]+dp[i-1][1]
    else:
        dp[i][0]+=dp[i-1][0]*2
        dp[i][1]+=dp[i-1][1]*2
print(dp[n-1][p])

