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
d=len(str(N))
ans=0
def dfs(nm,sm):
    if sm<=N and str(sm).count("7") and str(sm).count("5") and str(sm).count("3"):
        global ans
        ans+=1
    if nm==d:
        return
    dfs(nm+1,int(str(sm)+"7"))
    dfs(nm+1,int(str(sm)+"5"))
    dfs(nm+1,int(str(sm)+"3"))
    return
dfs(0,0)
print(ans)