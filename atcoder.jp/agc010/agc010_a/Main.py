def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def ZER(N): return [False for _ in range(N)]


INF = 10**30
MOD = 10**9+7


#          V
#     ／￣ψ￣＼
#    | 合格祈願 |
#    |＿＿＿＿＿|


##############################################################################

n=II()
A=LIIS()
if sum(A)%2:
    print("NO")
else:
    print("YES")