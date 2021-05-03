import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
N=II()
A=LIIS()
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
B=Bit(N)
ans=0
cnt=0
for I in range(N):
    B.add(A[I]+1,1)
    ans+=B.sum(N)-B.sum(A[I]+1)


print(ans)
for i in range(N-1):
    a=A[i]
    ans+=N-1-a*2
    print(ans)



