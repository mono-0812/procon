n=int(input())
A=list(map(int,input().split()))
mi=max(A)
ans=0
for i in range(n):
    for j in list(range(n))[i:]:
        if i==j:
            mi=A[i]
        mi=min(mi,A[j])
        ans=max(ans,mi*(j-i+1))
print(ans)