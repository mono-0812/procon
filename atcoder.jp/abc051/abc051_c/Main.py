import bisect,collections,copy,heapq,itertools,math,string,sys,queue
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
sx,sy,tx,ty=IIS()
x=abs(sx-tx);y=abs(sy-ty)
ans=""
for i in range(y): ans+="U"
for i in range(x): ans+="R"
for i in range(y): ans+="D"
for i in range(x+1): ans+="L"
for i in range(y+1): ans+="U"
for i in range(x+1): ans+="R"
ans+="D";ans+="R"
for i in range(y+1): ans+="D"
for i in range(x+1): ans+="L"
ans+="U"
print(ans)
