import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=998244353
##############################################################################
li=[0]*(10**5+100)
n,k=IIS()
for i in range(n):
    a,b=IIS()
    li[a]+=b
for i in range(len(li)):
    k-=li[i]
    if k<=0:
        print(i)
        exit()


