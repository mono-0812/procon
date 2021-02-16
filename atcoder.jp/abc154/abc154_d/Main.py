n,k=map(int,input().split())
P=list(map(int,input().split()))
pl=[0]*n
ans=0
import itertools
for i in range(n):
    pl[i]=(1+P[i])/2
plc=list(itertools.accumulate(pl))
if n==k:
    print(plc[-1])
    exit()
for i in range(0,n-k):
    total=plc[i+k]-plc[i]
    ans=max(total,ans)
print(ans)