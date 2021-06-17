import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
start_time=time.time()
def nt(): print(time.time()-start_time);return
def chmax(a: list, b: list) -> bool:
     assert len(a) == len(b) == 1, "1要素のlistを指定してください"
     if a[0] < b[0]:
         a[0] = b[0]
         return True
     return False
def chmin(a: list, b: list) -> bool:
    assert len(a) == len(b) == 1, "1要素のlistを指定してください"
    if a[0] > b[0]:
        a[0] = b[0]
        return True
    return False
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ragen=range
INF=10**10
MOD=10**9+7
from decimal import Decimal as d
##############################################################################
n,m=IIS()
li=[[] for i in range(n)]
for i in range(m):
    a,b=IIS()
    li[a-1].append(b-1)
    li[b-1].append(a-1)
ans=0
for to in range(n):
    for fr in range(to):
        used=[False for i in range(n)]
        q=collections.deque()
        q.append(0)
        used[0]=True
        f=False
        while len(q):
            x=q.popleft()
            for i in li[x]:
                if x==fr and i==to or x==to and i==fr:
                    f=True
                    continue
                if not used[i]:
                    q.append(i)
                    used[i]=True
        if sum(used)!=n and f:
            ans+=1
print(ans)
