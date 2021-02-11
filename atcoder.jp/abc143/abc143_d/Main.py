n=int(input())
L=list(map(int,input().split()))
from bisect import bisect_left
L.sort()
ans=0
for i in range(n):
    for j in range(i+1,n):
        b = bisect_left(L,L[i]+L[j])
        ans+=b-j-1
print(ans)
