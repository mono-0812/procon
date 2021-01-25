n,m,c = map(int,input().split())
B=list(map(int,input().split()))
cnt=0
for i in range(1,n+1):
  A=list(map(int,input().split()))
  total=0
  for r in range(m):
    total+=A[r]*B[r]
  total+=c
  if total>0:
    cnt+=1
print(cnt)