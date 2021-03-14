n=int(input())
s=input()
ans=0
for i in range(0,1000):
    val=str(i)
    while len(val)<3:
        val="0"+val
    cnt=0
    for j in s:
        if val[cnt]==j:
            cnt+=1
        if cnt==3:
            ans+=1
            break
print(ans)