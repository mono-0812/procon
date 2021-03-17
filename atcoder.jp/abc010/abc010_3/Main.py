import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
txa,tya,txb,tyb,T,V=IIS()
n=II()
for _ in range(n):
    x,y=IIS()
    if ((x-txa)**2+(y-tya)**2)**0.5+((x-txb)**2+(y-tyb)**2)**0.5<=T*V:
        print("YES")
        exit()
print("NO")