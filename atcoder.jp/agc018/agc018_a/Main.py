import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=998244353
##############################################################################
n,k=IIS()
A=LIIS()
gcd=math.gcd(A[0], A[-1])
for i in range(n):
    gcd=math.gcd(gcd, A[i])
if k%gcd or k>max(A):
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
