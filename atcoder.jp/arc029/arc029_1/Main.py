import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
t=[]
for _ in range(n): t.append(II())
ans=INF
T=sum(t)
def solve(num,sm):
    if num==n-1:
        global ans
        ans=min(ans,max(sm,(T-sm)))
        return 0
    solve(num+1,sm+t[num])
    solve(num+1,sm)
    return 0
solve(0,0)
print(ans)