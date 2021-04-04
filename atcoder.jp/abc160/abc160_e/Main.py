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

x,y,a,b,c=IIS()
A=LIIS();B=LIIS();C=LIIS()
A.sort(reverse=True);B.sort(reverse=True);C.sort()
A=A[:x];B=B[:y]
A+=B
A.sort()
ans=sum(A)
for a in A:
    c=C.pop()
    if a<c:
        ans+=c-a
    else:
        C.append(c)
    if len(C)==0:
        break
print(ans)