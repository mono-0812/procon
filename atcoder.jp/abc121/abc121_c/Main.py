n,m=map(int,input().split())
li=[]
cnt=0
ans=0
for i in range(n):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort()
for i in range(m):
    if li[cnt][1]==0:
        cnt+=1
    ans+=li[cnt][0]
    li[cnt][1]-=1
print(ans)