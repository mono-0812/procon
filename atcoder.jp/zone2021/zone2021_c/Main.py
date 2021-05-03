import bisect,collections,copy,heapq,itertools,math,string,sys,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
n=II()
li=[LIIS() for i in range(n)]
l=0
r=1001001001
def ok(v):
    zo=copy.deepcopy(li)
    st=[]
    for i in range(n):
        for j in range(5):
            if zo[i][j]>=v:zo[i][j]=True
            else:zo[i][j]=False
        if not zo[i] in st:
            st.append(zo[i])
    for i in range(len(st)):
        for j in range(len(st)):
            for k in range(len(st)):
                vs=[]
                for s in range(5):
                    vs.append(st[i][s]+st[j][s]+st[k][s])
                f=0
                for s in range(5):
                    if vs[s]:f+=1
                if f==5:return True
    return False
while r-l>=2:
    mid=(r+l)//2
    if ok(mid):l=mid
    else:r=mid
print(l)
