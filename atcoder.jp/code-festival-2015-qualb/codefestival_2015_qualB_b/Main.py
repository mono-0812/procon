import bisect,collections,copy,heapq,operator,itertools,math,string,sys
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
AD=collections.Counter(A)
for i in A:
    if AD[i]>n/2:
        print(i)
        exit()
print("?")