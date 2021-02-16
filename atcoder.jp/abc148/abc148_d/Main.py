n=int(input())
A=list(map(int,input().split()))
val=1
ans=0
for i in A:
    if val==i:
        val+=1
    else:
        ans+=1
if ans==len(A):
    print(-1)
    exit()
print(ans)