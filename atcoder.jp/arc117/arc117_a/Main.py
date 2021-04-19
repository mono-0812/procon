import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=998244353
import decimal
##############################################################################
a,b=IIS()
ans=[]
val=1
for i in range(a-1):
    ans.append(val)
    val+=1
val2=-1
for i in range(b-1):
    ans.append(val2)
    val2-=1
a-=1;b-=1
if ((1+a)*(a)//2)-((1+b)*(b)//2)>0:
    ans+=[(((1+a)*a//2)-((1+b)*(b)//2))*-1+val*-1]
    ans+=[val]
elif ((1+a)*a//2)-((1+b)*(b)//2)<0:
    ans+=[abs(((1+a)*a//2)-((1+b)*(b)//2))+val2*-1]
    ans+=[val2]
else:
    ans+=[max(abs(val),abs(val2)),max(abs(val),abs(val2))*-1]

print(*ans)


