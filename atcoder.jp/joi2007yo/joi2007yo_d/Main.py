import bisect,collections,copy,heapq,operator,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
def refle(li):
    res=[]
    for i in range(len(li)//2):
        res.append(li[i])
        res.append(li[i+len(li)//2])
    return res
def cut(li,k):
    return li[k:]+li[:k]
N=II();M=II()
deck=list(range(1,1+2*N))
for _ in range(M):
    K=II()
    if K==0:
        deck=refle(deck)
    else:
        deck=cut(deck,K)
for i in deck:
    print(i)