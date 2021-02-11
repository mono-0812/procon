n=int(input())
A=list(map(int,input().split()))
import collections
AC=collections.Counter(A)
vals=list(set(A))
ans=0
for i in vals:
    if i>AC[i]:
        ans+=AC[i]
    if i<AC[i]:
        ans+=AC[i]-i
print(ans)

