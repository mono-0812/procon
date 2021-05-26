def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
##############################################################################
n=II()
D=LIIS()
mod=998244353
li=[0 for i in range(max(D)+1)]
for i in range(n):
    li[D[i]]+=1
ans=1
if li[0]!=1:print(0);exit()
if D[0]!=0:print(0);exit()
for i in range(len(li)):
    if li[i]==0:
        print(0)
        exit()
    else:
        if i<2:continue
        else:ans=(ans*pow(li[i-1],li[i],mod))%mod
print(ans%mod)