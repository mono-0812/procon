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
    odd=0
    even=0
    i = 1
    while i*i <= n:
        if n % i == 0:
            if i%2==0:
                even+=1
            else:
                odd+=1
            if i != n // i:
                if (n//2)%2==0:
                    even+=1
                else:
                    odd+=1
        i += 1
    return (even,odd)

#　　　　　V
#　　 ／￣ψ￣＼
#　　| 合格祈願 |
#　　|＿＿＿＿＿|

##############################################################################
n,a,b=IIS()
X=LIIS()
ans=0
for i in range(n-1):
    ans+=min(b,a*(X[i+1]-X[i]))
print(ans)
