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


n,m=IIS()
li=[[] for _ in range(n)]
for i in range(m):
    p,y=IIS()
    li[p-1].append((y,i,p))
li=[sorted(li[_],key=lambda a:a[0]) for _ in range(n)]
ans=[0 for _ in range(m)]
for i in li:
    for j in range(len(i)):
        y,num,p=i[j]
        ans[num]=str(p).zfill(6)+str(j+1).zfill(6)
print(*ans)