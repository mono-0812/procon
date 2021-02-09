n,m=map(int,input().split())
A=list(map(int,input().split()))
import math
if m==0:
    print(1)
    exit()
lasa=0
k=max(A)
li=[]
ans=0
A.sort()
for a in A:
    if a==1:
        lasa=a
        continue
    if a-lasa-1 > 0:
        k=min(k,a-lasa-1)
    li.append(a-lasa-1)
    lasa=a
li.append(n-lasa)
for i in li:
    ans+=math.ceil(i/k)
print(ans)
