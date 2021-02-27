n=int(input())
li=[]
for i in range(n):
    a,p,x=map(int,input().split())
    li.append((a,p,x))
ans=1000000000
for a,p,x in li:
    A=x-0.5
    if a>A:
        continue
    ans=min(ans,p)
if ans==1000000000:
    print(-1)
else:
    print(ans)

    