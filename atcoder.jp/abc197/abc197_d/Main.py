import bisect,collections,copy,heapq,itertools,math,string,sys,queue
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
##############################################################################
from decimal import Decimal
n=Decimal(input())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
xs=(x2+x1)/2
ys=(y2+y1)/2

x1-=xs;y1-=ys
kakudo=360/n
print((x1*math.cos(math.radians(kakudo))-y1*math.sin(math.radians(kakudo))+xs),(x1*math.sin(math.radians(kakudo))+y1*math.cos(math.radians(kakudo)))+ys)
