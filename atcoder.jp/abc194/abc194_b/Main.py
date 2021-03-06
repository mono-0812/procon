n=int(input())
A=[]
B=[]
ans=float("inf")
for i in range(n):
    a,b=map(int,input().split())
    ans=min(ans,a+b)
    A.append(a)
    B.append(b)
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        ans=min(ans,max(A[i],B[j]))
print(ans)