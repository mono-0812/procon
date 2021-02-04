n=int(input())
B=list(map(int,input().split()))
A=[]
for i in range(n):
    if i==0:
        A.append(B[i])
        continue
    if i==n-1:
        A.append(B[len(B)-1])
        continue
    A.append(min(B[i-1],B[i]))
print(sum(A))