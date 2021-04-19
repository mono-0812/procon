import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=998244353
##############################################################################
n,m=IIS()
li=[]
for i in range(m):
    li.append(LIIS()[1:])
p=LIIS()
ans=0
def dfs(num,sw):
    if num==n:
        for i in range(m):
            val=0
            for j in li[i]:
                val+=sw[j-1]
            if not val%2==p[i]%2:
                return
        global ans
        ans+=1
        return
    dfs(num+1,sw+[1])
    dfs(num+1,sw+[0])
    return
dfs(0,[])
print(ans)



