import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
S=I()
flag=0
cnt=0
for i in S:
    if i=="T" and flag:
        cnt+=1
        flag-=1
        continue
    if i=="S":
        flag+=1
        continue
print(len(S)-cnt*2)


