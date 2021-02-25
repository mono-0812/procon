n=int(input())
P=list(map(int,input().split()))
PS=sorted(P)
cnt=0
for i in range(n):
    if PS[i]!=P[i]:
        cnt+=1
if cnt > 2:
    print("NO")
else:
    print("YES")