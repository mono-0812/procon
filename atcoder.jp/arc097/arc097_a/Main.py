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
s=I()
k=II()
li=[]
for i in range(len(s)):
    for j in range(min(len(s)-i,k)):
        li.append(s[i:i+j+1])
li=list(set(li))
li.sort()
print(li[k-1])

