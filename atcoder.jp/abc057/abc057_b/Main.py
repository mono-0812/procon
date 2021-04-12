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

import math
##############################################################################
st=[]
mh=[]
n,m=IIS()
for i in range(n):
    a,b=IIS()
    st.append((a,b))
for i in range(m):
    c,d=IIS()
    mh.append((c,d))
ans=[]
for i in range(n):
    val=INF
    num=0
    a,b=st[i]
    for j in range(m):
        c,d=mh[j]
        if abs(a-c)+abs(b-d)<val:
            val=abs(a-c)+abs(b-d)
            num=j+1
    ans.append(num)
print(*ans)

