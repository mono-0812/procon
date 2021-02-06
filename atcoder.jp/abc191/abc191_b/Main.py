#n=int(input())
n,x=map(int,input().split())
A=list(map(int,input().split()))
ans=[]
for i in A:
    if i!=x:
        ans.append(i)
print(*ans)
