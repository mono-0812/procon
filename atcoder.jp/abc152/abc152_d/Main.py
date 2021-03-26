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
dic=dict()
n=II()
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)
for i in range(1,n+1):
    f=int(str(i)[0])
    e=int(str(i)[-1])
    dic[(f,e)]=(dic.get((f,e)) if dic.get((f,e)) else 0)+1
ans=0
for i,j in dic.keys():
    try:ans+=dic[(i,j)]*dic[(j,i)]
    except:continue
print(ans)