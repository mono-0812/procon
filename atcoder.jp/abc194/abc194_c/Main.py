n=int(input())
A=list(map(int,input().split()))
ans=0
smA=sum(A)
for i in A:
    ans+=(i**2)*(n-1)
for i in A:
    smA-=i
    ans-=i*smA*2
print(abs(ans))