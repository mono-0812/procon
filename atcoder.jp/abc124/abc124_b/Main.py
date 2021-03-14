n=int(input())
H=list(map(int,input().split()))
mx=0
ans=0
for i in H:
    if mx<=i:
        ans+=1
    mx=max(mx,i)
print(ans)