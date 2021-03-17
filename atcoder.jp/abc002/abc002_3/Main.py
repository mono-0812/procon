import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
x1,y1,x2,y2,x3,y3=IIS()
print(0.5*abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)))