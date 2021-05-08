import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
n,m=IIS()
path=[[] for i in range(n)]
for i in range(m):
    a,b=IIS()
    path[a-1].append(b-1)
    path[b-1].append(a-1)
k=II()
C=LIIS()
def bfs(s):
    cost=[INF]*n
    cost[s]=0
    q=queue.deque([s])
    while q:
        x=q.popleft()
        for y in path[x]:
            if cost[y]>cost[x]+1:
                cost[y]=cost[x]+1
                q.append(y)
    return [cost[c-1] for c in C]
D=[bfs(c-1) for c in C]
dp=[[INF]*(k) for i in range(pow(2,k))]#[どこに行ったか][直前に行ったところ]
for i in range(k):
    dp[0][i]=0
for bit in range(1<<k):
    for j in range(k):
        if bit|(1<<j)==1<<j:
            dp[bit|(1<<j)][j]=1
        elif not (bit&(1<<j)):
            for l in range(k):
                if (bit&(1<<l)):#12いってねぇよ　もらうかくばるかはっきり
            #iが今どこまで言ったか　j がto lがfrom
                    dp[bit|(1<<j)][j]=min(dp[bit|(1<<j)][j],dp[bit][l]+D[l][j])
ans=INF
for i in range(k):
    ans=min(ans,dp[-1][i])
if ans==INF:
    print(-1)
else:
    print(ans)
