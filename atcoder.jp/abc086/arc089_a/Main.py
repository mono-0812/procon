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

N=II()
lx=0
ly=0
lt=0
for i in range(N):
    t,x,y=IIS()
    if abs(t-lt) >= abs(lx-x) + abs(ly-y) and abs(t-lt)%2==(abs(lx-x) + abs(ly-y))%2:lx=x;ly=y;lt=t;continue
    print("No");exit()

print("Yes")