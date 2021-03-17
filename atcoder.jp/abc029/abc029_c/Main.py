import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
li=[]
def solve(num,pas):
    if num==n:
        global li
        li.append(pas)
        return 0
    solve(num+1,pas+"a")
    solve(num+1,pas+"b")
    solve(num+1,pas+"c")
    return 0
solve(0,"")
li.sort()
for i in li:
    print(i)