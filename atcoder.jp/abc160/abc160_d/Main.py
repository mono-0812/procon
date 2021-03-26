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
n,x,y=IIS()
x-=1;y-=1
ans=[0]*(n)
for i in range(n):
    for j in range(n):
        if not i<j:continue
        val=j-i
        if abs(x-i)<abs(y-i):
            val2=abs(x-i)+abs(y-j)+1
        else:
            val2=abs(y-i)+abs(x-j)+1
        ans[min(val,val2)]+=1
print(*ans[1:])