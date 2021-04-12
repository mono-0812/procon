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
h,w=IIS()
f=[[] for _ in range(h)]
for i in range(h):
    s=I()
    for j in range(w):
        f[i].append(s[j])

def dfs(H,W):
    val=0
    global f
    for i in [1,0,-1]:
        for j in [1,0,-1]:
            if i==j==0:continue
            if 0<=H+i<h and 0<=W+j<w:
                if f[H+i][W+j]=="#":
                    val+=1
    if f[H][W]!="#":
        f[H][W]=val
    return
for i in range(h):
    for j in range(w):
        dfs(i,j)
for i in f:
    print("".join(map(str,i)))
