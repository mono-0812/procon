import bisect,collections,copy,heapq,itertools,math,string,sys,queue
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=10**10
MOD=998244353
##############################################################################
s=I()
S=""
for i in reversed(s):
    S=i+S
    if S in ("dream","dreamer","erase","eraser"):
        S=""
if len(S):
    print("NO")
else:
    print("YES")