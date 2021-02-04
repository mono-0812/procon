n=int(input())
H=list(map(int,input().split()))
lash=0
cnt=0
ans=0
for i in H:
    if lash>=i:
        cnt+=1
        ans=max(ans,cnt)
        lash=i
    else:
        lash=i
        cnt=0
print(ans)