import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
ans=[]
def solve(num,val,a):
    if num==n:
        print(a)
        return
    for i in range(val):
        solve(num+1,max(val,i+2),a+chr(i+ord("a")))
    return
solve(0,1,"")