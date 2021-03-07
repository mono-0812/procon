n=int(input())
ans=0
val=n//11
ans+=(n//11)*2
if n-11*(val)>0:
    n-=6
    ans+=1
if n-11*(val)>0:
    n-=5
    ans+=1
print(ans)