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
n=II()
A=LIIS()
A.sort()
Amax=A[-1]
dp=[1]*(Amax+1)
ans=0
for i in range(len(A)-1):
    p=A[i]
    if dp[p]==1:
        for q in range(Amax//p+1):
            dp[p*q]=0
        if A[i]!=A[i+1]:
            ans+=1
if dp[Amax]==1:
    ans+=1
print(ans)