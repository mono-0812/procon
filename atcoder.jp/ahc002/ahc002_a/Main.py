import bisect,collections,copy,heapq,itertools,math,string,sys,random,decimal,queue
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
import time
start=time.time()
now=time.time()
T=0
from math import exp
##############################################################################
si,sj=IIS()
si,sj=sj,si
t=[LIIS() for i in range(50)]
p=[LIIS() for i in range(50)]
DRUL={(1,0):"D",(0,1):"R",(-1,0):"U",(0,-1):"L"}
def can_go(X,Y):
    res=[]
    for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=X+i<50 and 0<=Y+j<50:
            if used[Y+j][X+i]:
                res.append((X+i,Y+j))
    return res
answer=[]
mxpoint=0
start_temp=100
end_temp=5
def temperature(tm, limit):
    x = tm / limit
    return pow(start_temp, 1 - x) * pow(end_temp, x)
def prob(new_score, TM, LIMIT):
    d = new_score
    if d>=0:
        return 1
    return exp(d / temperature(TM, LIMIT))
while now-start<1.6:
    used=[[True for _ in range(50)] for i in range(50)]#Trueは使われてない#zero-index?
    ans=[(si,sj)]
    tmp=[]
    used[sj][si]=False
    for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=si+i<50 and 0<=sj+j<50:
            if t[sj][si]==t[sj+j][si+i]:
                used[sj+j][si+i]=False
                break
    point=p[sj][si]

    while True:
        x,y=ans[-1]
        li=can_go(x,y)
        if len(li)==0:break
        li.sort(key=lambda x: p[x[1]][x[0]])
        PP=list(map(lambda x: p[x[1]][x[0]]-p[li[-1][1]][li[-1][0]],li))
        for i in range(len(li)):
            if prob(PP[i],now-start,1.6)>random.random():
                gx,gy=li[i]
                break
        ans.append((gx,gy))
        used[gy][gx]=False
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=gx+i<50 and 0<=gy+j<50:
                if t[gy][gx]==t[gy+j][gx+i]:
                    used[gy+j][gx+i]=False
                    break
        tmp.append(DRUL[(gy-y,gx-x)])
        point+=p[y][x]
    if mxpoint<point:
        answer=tmp
        mxpoint=point
    now=time.time()
print("".join(answer))


