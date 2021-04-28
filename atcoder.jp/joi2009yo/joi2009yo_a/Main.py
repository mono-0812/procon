import bisect,collections,copy,heapq,itertools,math,string,sys,queue,datetime,time
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
for i in range(3):
    a,b,c,d,e,f=IIS()
    print(" ".join(map(str,map(int,(str(datetime.datetime(year=1,month=1,day=1,hour=d,minute=e,second=f)-datetime.datetime(year=1,month=1,day=1,hour=a,minute=b,second=c))).split(":")))))
