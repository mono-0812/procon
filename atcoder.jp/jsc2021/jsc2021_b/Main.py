import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n,m=IIS()
A=LIIS()
B=LIIS()
B=set(B)
ans=[]
for i in A:
    if i in B:
        ans.append(i)
ans=set(ans)
anss=list(set(A+list(B)))
anss.sort()
for i in anss:
    if not i in ans:
        print(i)

