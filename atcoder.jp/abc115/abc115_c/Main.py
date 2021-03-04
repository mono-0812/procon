n,k=map(int,input().split())
H=[]
for _ in range(n): H.append(int(input()))
H.sort()
ans=float("inf")
for i in range(n-k+1):
    ans=min(ans,H[i+k-1]-H[i])
print(ans)