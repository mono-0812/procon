import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
N,M,X,Y=IIS()
X-=1; Y-=1
edge = [[] for _ in range(N)]
for _ in range(M):
    a,b,t,k=IIS()
    a-=1;b-=1
    edge[a].append((b,t,k))
    edge[b].append((a,t,k))
path=[-1]*N
q=[(0,X)]
while q:
    t,v = heapq.heappop(q)
    if path[v]==-1:
        path[v]=t
        if v==Y:
            break
        for nv,T,K in edge[v]:
            d=(K-(t%K))%K
            nt=t+d+T
            heapq.heappush(q,(nt,nv))
print(path[Y])