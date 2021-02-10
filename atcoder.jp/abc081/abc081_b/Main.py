n=int(input())
A=list(map(int,input().split()))
sma=sum(A)
ans=0
flag=True
while flag:
    for i in range(n):
        if A[i]%2==1:
            flag=False
            break
        else:
            A[i]=A[i]//2
    if flag==False:
        break
    ans+=1
print(ans)