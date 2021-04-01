def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
def ZER(N): return [False for _ in range(N)]
INF=float("inf")
MOD=10**9+7
#　　　　　V
#　　 ／￣ψ￣＼
#　　| 合格祈願 |
#　　|＿＿＿＿＿|
##############################################################################
x,y=IIS()
ans=INF
for i in range(2):
    for j in range(2):
        vx,vy=x,y
        if i:
            vx=x*-1
        if j:
            vy=y*-1
        if vy >= vx:
            ans=min(ans,vy-vx+i+j)
    
print(ans)