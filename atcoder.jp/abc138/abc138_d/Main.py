import bisect,collections,copy,heapq,itertools,math,string,sys,decimal,queue
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
N,Q=IIS()
G=[[] for _ in range(N)]
for i in range(N-1):
    a,b=IIS()
    G[a-1].append(b-1)
    G[b-1].append(a-1)
X=[0 for i in range(N)]
for i in range(Q):
    p,x=IIS()
    X[p-1]+=x
q=[0]
reseached=[0 for i in range(N)]
ans=[0 for i in range(N)]
while q:
    r=q.pop()
    ans[r]+=X[r]
    reseached[r]=1
    for p in G[r]:
        if reseached[p]==0:
            ans[p]+=ans[r]
            q.append(p)
print(*ans)