import bisect,collections,copy,heapq,itertools,math,string,sys,decimal,queue
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
n,k=IIS();A=LIIS()
t_zero=[-1]*n
t=0
a=1
while t_zero[a-1]==-1:
    if t==k:
        break
    t_zero[a-1]=t
    t+=1
    a=A[a-1]
else:
    k=(k-t_zero[a-1])%(t-t_zero[a-1])
    a=t_zero.index(t_zero[a-1]+k)+1
print(a)