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
n=II();s=I()
r=s.count("R");g=s.count("G");b=s.count("B")
ans=r*g*b
for i in range(n):
    for d in range(n):
        j=i+d
        k=i+2*d
        if k>=n:
            break
        if s[i]!=s[j]and s[i]!=s[k] and s[j]!=s[k]:
            ans-=1
print(ans)