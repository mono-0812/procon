import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=10**9+7
sys.setrecursionlimit(10**8)
##############################################################################
n=II()
A=LIIS()
x=0
for a in A:
    x^=a
for a in A:
    print(a^x)