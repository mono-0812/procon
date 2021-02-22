n,m=map(int,input().split())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))
val=0
ans=0
for i in range(m):
    for j in range(m):
        val=0
        for k in range(n):
            val+=max(li[k][i],li[k][j])
        ans=max(val,ans)
print(ans)
