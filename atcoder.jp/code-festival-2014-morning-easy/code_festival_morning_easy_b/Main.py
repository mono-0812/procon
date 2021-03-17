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
flag=1
for i in range(0,200,20):
    if i+1<=n<=i+20:
        if flag==1:
            print((n-1)%20+1)
        else:
            if n%20==0:
                print(1)
                exit()
            print(20-(n%20)+1)
        exit()
    flag*=-1