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
x1,y1,x2,y2=IIS()
mx=x2-x1;my=y2-y1
print(x2-my,y2+mx,x1-my,y1+mx)