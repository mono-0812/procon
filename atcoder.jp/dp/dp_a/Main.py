import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
############################################
n=II()
H=LIIS()
dp=[INF]*n
dp[0]=0
dp[1]=abs(H[1]-H[0])
for i in range(2,n):
    dp[i]=min(dp[i-1]+abs(H[i]-H[i-1]),dp[i-2]+abs(H[i]-H[i-2]))
print(dp[n-1])


