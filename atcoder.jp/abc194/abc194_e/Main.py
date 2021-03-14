import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
############################################
n,m=IIS()
A=LIIS()
mex=INF
lis=[False for _ in range(n+10)]+[mex]
ans=[True for _ in range(n+10)]
for i in A[:m]:
    lis[i]+=True
    ans[i]=False
#for i in range(n+10):
#   if lis[i]:continue
#    ans=min(ans,i)
#    break
for i in range(1,n-m+1):
    mi=A[i-1]
    mx=A[i+m-1]
    lis[mi]-=1
    lis[mx]+=1
    if lis[mi]==0:
        ans[mi]=True
for i in range(len(ans)):
    if ans[i]:
        print(i)
        exit()

    
