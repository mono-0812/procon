def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def ZER(N): return [False for _ in range(N)]


INF = 10**30
MOD = 10**9+7


#         V
#    ／￣ψ￣＼
#   | 合格祈願 |
#   |＿＿＿＿＿|


##############################################################################
n=II()
li=[0]*(10**3+100)
def prime_factorize(n):
    global li
    while n % 2 == 0:
        li[2]+=1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            li[f]+=1
            n //= f
        else:
            f += 2
    if n != 1:
        li[n]+=1
    return
for i in range(2,n+1):
    prime_factorize(i)
ans=1
for i in li:
    ans*=(i+1)
print(ans%MOD)


