import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
a,b,c,x,y=IIS()
c=min(c*2,a+b)
if x<y:
    print(min(x*c+(y-x)*b,y*c))
elif x>y:
    print(min(y*c+(x-y)*a,x*c))
else:
    print(x*c)
