import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
class Dijkstra:
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d):
        self.e[u].append([v, d])
        self.e[v].append([u, d])

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

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d
n=II()
D=Dijkstra()
for _ in range(n-1):
    a,b,c=IIS()
    D.add(a,b,c)
q,k=IIS()
klis=D.search(k)
for _ in range(q):
    x,y=IIS()
    print(klis[x]+klis[y])

