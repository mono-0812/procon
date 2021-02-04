n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
total=0
for i in range(n):
    if A[i] >= B[i]:
        total+=B[i]
    else:
        total+=A[i]
        if A[i+1]<=B[i]-A[i]:
            total+=A[i+1]
            A[i+1]=0
        else:
            total+=B[i]-A[i]
            A[i+1]-=B[i]-A[i]
print(total)

