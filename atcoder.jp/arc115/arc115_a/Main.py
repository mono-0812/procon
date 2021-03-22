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
odd=0
even=0
for i in range(n):
    val=sum(map(int,I()))
    if val%2:odd+=1
    else:even+=1
print(odd*even)
