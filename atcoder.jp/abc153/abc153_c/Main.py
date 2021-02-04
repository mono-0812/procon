n,k=map(int,input().split())
H=list(map(int,input().split()))
if k>=n:
    print(0)
    exit()
H.sort(reverse=True)
ans=sum(H)
for i in range(k):
    ans-=H[i]
print(ans)
