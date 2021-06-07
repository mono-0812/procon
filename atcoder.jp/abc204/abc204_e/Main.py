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
import collections
import heapq
def dis(tim,D):
    if tim<=round(D**0.5)-1:
        return D//(round(D**0.5))+(round(D**0.5)-tim-1)
    return D//(tim+1)

class Dijkstra:
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d,c):
        self.e[u].append([v, d,c])
        self.e[v].append([u, d,c])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def search(self, s):
        """
        :param s: 始点
        :return: 始点から各点までの最短経路
        """
        d = collections.defaultdict(lambda: float('inf'))
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud ,uc in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud + dis(k,uc)
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d
Dijk=Dijkstra()
N,m=IIS()
for i in range(m):
    a,b,c,d=IIS()
    Dijk.add(a,b,c,d)
print(Dijk.search(1)[N] if Dijk.search(1)[N]!=float("inf") else -1)
