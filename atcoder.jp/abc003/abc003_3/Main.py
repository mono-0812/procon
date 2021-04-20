import bisect,collections,copy,heapq,itertools,math,string,sys,random
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
import decimal
##############################################################################
n,k=IIS()
li=LIIS()
li.sort(reverse=True)
li=li[:k]
li=li[::-1]
rate=0
for i in range(k):
    rate=(li[i]+rate)/2
print(rate)