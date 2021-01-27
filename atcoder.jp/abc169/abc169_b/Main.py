n=int(input())
A=list(map(int,input().split()))
total=1
if 0 in A:
  print(0)
  exit()
for a in A:
  total*=a
  if total > 10**18:
    print(-1)
    exit()
print(total)