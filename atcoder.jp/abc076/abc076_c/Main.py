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


s=I();t=I()
li=[]
import re
for i in range(len(s)-len(t)+1):
    val=s[i:i+len(t)]
    f=True
    for j in range(len(val)):
        if not t[j]==val[j] and not val[j]=="?":
            f=False
            break
    if f:
        val=list(s[:i]+t+s[i+len(t):])
        for i in range(len(val)):
            if val[i]=="?":
                val[i]="a"

        li.append("".join(val))
li=list(set(li))
li.sort()
if len(li)==0:
    print("UNRESTORABLE")
    exit()
print(li[0])