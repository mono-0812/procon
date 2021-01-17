n = int(input())
cnt = 0
ans = 0
for i in range(1,n+1):
  for a in str(i):
    cnt+=1
  if cnt %2 ==1:
    ans+=1
  cnt=0
print(ans)