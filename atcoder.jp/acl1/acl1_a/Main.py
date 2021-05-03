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
n=II()
x2i=[0]*n
i2y=[0]*n
for i in range(n):
    a,b=IIS()
    x2i[n-a]=i
    i2y[i]=b-1
ans=[0]*n
pre=0
mx=0
for x in range(n):
    i=x2i[x]
    y=i2y[i]
    mx=max(mx,y)
    if mx == x:
        for p in range(pre,x+1):
            ans[x2i[p]]=x+1-pre
        pre=x+1
print(*ans)