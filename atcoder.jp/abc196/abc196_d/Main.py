import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
##############################################################################
h,w,a,b=IIS()
used=[[0]*w for _ in range(h)]
res=0
def dfs(i,j,a,b):
    global res
    if a<0 or b<0:
        return
    if j==w:
        j=0
        i+=1
    if i==h:
        res+=1
        return
    if used[i][j]==1:
        return dfs(i,j+1,a,b)
    used[i][j]=1
    dfs(i,j+1,a,b-1)
    if j+1 < w and used[i][j+1]==0:
        used[i][j+1]=1
        dfs(i,j+1,a-1,b)
        used[i][j+1]=0
    if i+1<h and used[i+1][j]==0:
        used[i+1][j]=1
        dfs(i,j+1,a-1,b)
        used[i+1][j]=0
    used[i][j]=0
    return res
print(dfs(0,0,a,b))

