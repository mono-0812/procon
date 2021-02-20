from heapq import heappush,heappop
N,M=map(int,input().split())
edge = [[] for _ in range (2*N)]
for _ in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    edge[a].append((b,c))
ans = [-1] * N
path = [-1] * (2*N)
for i in range(N):
    q=[]
    for nv,c in edge[i]:
        heappush(q,(c,nv))
    while q:
        s,v=heappop(q)
        if v == i:
            ans[i]=s
            break
        elif path[v]<i:
            path[v]=i
            for nv,c in edge[v]:
                ns = s+c
                heappush(q,(ns,nv))
print(*ans,sep="\n")