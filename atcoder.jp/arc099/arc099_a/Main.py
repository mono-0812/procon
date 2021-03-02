n,k=map(int,input().split())
A=list(map(int,input().split()))
val=1
ans=0
while val<n:
    val+=k-1
    ans+=1
print(ans)
