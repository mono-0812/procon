import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
x1,y1,r=IIS()
x2,y2,x3,y3=IIS()
if x2<=x1-r and x1+r<=x3 and y2<=y1-r and y1+r<=y3:
    print("NO")
else:
    print("YES")
def ok(A,B):
    if (x1-A)**2 + (y1-B)**2<r**2:
        return True
    return False
if ok(x2,y2) and ok(x2,y3) and ok(x3,y2) and ok(x3,y3):
    print("NO")
else:
    print("YES")