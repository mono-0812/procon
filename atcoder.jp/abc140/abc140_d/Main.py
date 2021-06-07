import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time
import numpy as np
input = lambda: sys.stdin.readline().rstrip()
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def debug(*args): print(*args) if len(args)>0 else print(False);return
start_time=time.time()
def nt(): print(time.time()-start_time);return
def chmax(a: list, b: list) -> bool:
     assert len(a) == len(b) == 1, "1要素のlistを指定してください"
     if a[0] < b[0]:
         a[0] = b[0]
         return True
     return False
def chmin(a: list, b: list) -> bool:
    assert len(a) == len(b) == 1, "1要素のlistを指定してください"
    if a[0] > b[0]:
        a[0] = b[0]
        return True
    return False
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ragen=range
INF=10**10
MOD=10**9+7
from decimal import Decimal as d
##############################################################################
#間にあるやつの個数*2
#奇数の場合最後は*1
n,k=IIS()
s=I()
def rle(SEQ):
    res=[[1,SEQ[0]]]
    for i in range(1,len(SEQ)):
        if res[-1][1]==SEQ[i]:
            res[-1][0]+=1
        else:
            res.append([1,SEQ[i]])
    return res
li=rle(list(s))
ans=0
for i,j in li:
    ans+=(i-1)
print(min(k*2+ans,n-1))