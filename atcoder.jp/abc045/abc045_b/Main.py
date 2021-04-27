import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
A=list(I());B=list(I());C=list(I())
dic={"a":0,"b":1,"c":2}
turn=0
while True:
    if turn==0:
        if len(A)==0:
            print("A");exit()
        turn=dic[A.pop(0)]

    elif turn==1:
        if len(B)==0:
            print("B");exit()
        turn=dic[B.pop(0)]

    else:
        if len(C)==0:
            print("C");exit()
        turn=dic[C.pop(0)]
