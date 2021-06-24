import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
N,k=IIS()
A=LIIS();F=LIIS()
A.sort();F.sort(reverse=True)
ng=-1
ok=max([A[i]*F[i] for i in range(N)])

def is_ok(n):
    cnt=0
    for i in range(N):
        #print(i)
        cnt+=max(0,A[i]-math.floor(n/F[i]))
    return cnt<=k



while ok-ng>1:
    mid=(ng+ok)//2
    if is_ok(mid):
        ok=mid
    else:
        ng=mid
print(ok)