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
n=II()
sys.setrecursionlimit(1000000)
C=LIIS()
v=[[] for i in range(n)]
for i in range(n-1):
    a,b=IIS()
    v[a-1].append(b-1)
    v[b-1].append(a-1)

ans=[]
def dfs(p,x,color):

    if not color[C[x]]:
        global ans
        ans.append(x+1)
    if len(v[x])==1:
        if color[C[v[x][0]]]==p:pass
        else:color[C[x]]+=1
    else:color[C[x]]+=1

    for i in v[x]:
        if i==p:continue
        dfs(x,i,color)
    color[C[x]]-=1
    return 0
col=[0]*(10**5+30)
dfs(-1,0,col)
ans.sort()
print(*ans)


