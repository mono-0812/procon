import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
ragen=range
INF=10**10
MOD=10**9+7
##############################################################################
h,w=IIS()
F=[list(I()) for i in range(h)]
L=[[0]*w for i in range(h)]
R=[[0]*w for i in range(h)]
U=[[0]*w for i in range(h)]
D=[[0]*w for i in range(h)]
for i in range(h):
    cnt=0
    for j in range(w):
        if F[i][j]=="#":
            cnt=0
            continue
        L[i][j]=cnt
        cnt+=1
for i in range(h):
    cnt=0
    for j in range(w)[::-1]:
        if F[i][j]=="#":
            cnt=0
            continue
        R[i][j]=cnt
        cnt+=1
for j in range(w):
    cnt=0
    for i in range(h):
        if F[i][j]=="#":
            cnt=0
            continue
        D[i][j]=cnt
        cnt+=1
for j in range(w):
    cnt=0
    for i in range(h)[::-1]:
        if F[i][j]=="#":
            cnt=0
            continue
        U[i][j]=cnt
        cnt+=1
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,R[i][j]+L[i][j]+U[i][j]+D[i][j])
print(ans+1)