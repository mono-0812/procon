n=int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
mx=0
for i in range(n):
  if i==0:
    mx=sum(A2)+A1[0]
    continue
  mx = max(mx,sum(A1[:i+1])+sum(A2[i:]))
print(mx)