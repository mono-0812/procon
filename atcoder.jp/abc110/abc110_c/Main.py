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
T=I()
li=[set() for _ in range(27)]
li2=[set() for _ in range(27)]
for i in range(len(S)):
    li[ord(T[i])-97].add(S[i])
    li2[ord(S[i])-97].add(T[i])
for i in range(27):
    if len(li[i])>1 or len(li2[i])>1:
        print("No")
        exit()
print("Yes")
