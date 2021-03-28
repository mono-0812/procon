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

#　　　　　V
#　　 ／￣ψ￣＼
#　　| 合格祈願 |
#　　|＿＿＿＿＿|

##############################################################################
s=I();t=I()
dp=[[""]*(len(t)+10) for _ in range(len(s)+10)]
val=0
for i in range(len(s)):
    for j in range(len(t)):
        if s[i]==t[j]:
            if len(dp[i][j]+s[i])>max(len(dp[i+1][j]),len(dp[i][j+1])):
                dp[i+1][j+1]=dp[i][j]+s[i]
            else:
                if len(dp[i+1][j])>len(dp[i][j+1]):
                    dp[i+1][j+1]=dp[i+1][j]
                else:
                    dp[i+1][j+1]=dp[i][j+1]
        else:
            if len(dp[i+1][j])>len(dp[i][j+1]):
                    dp[i+1][j+1]=dp[i+1][j]
            else:
                dp[i+1][j+1]=dp[i][j+1]
        val=max(len(dp[i+1][j+1]),val)
for i in dp:
    for j in i:
        if len(j)==val:
            print(j)
            exit()
    