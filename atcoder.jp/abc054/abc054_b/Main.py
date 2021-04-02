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
A=[]
B=[]
for i in range(n):
    A.append(I())
for i in range(m):
    B.append(I())
ans=0
for i in range(n-m+1):
    for j in range(n-m+1):
        f=[]
        for k in range(j,j+m):
            f.append(A[k][i:i+m])
        if f==B:
            ans+=1
print("YNeos"[not ans::2])
