from itertools import combinations
n = list(map(int,input()))
mx=-1
if sum(n)%3==0:
  print(0)
  exit()
for i in range(1,len(n)):
  for comb in combinations(n, i):
    if sum(comb)%3==0:
      mx=i
if mx==-1:
  print(-1)
  exit()
print(len(n)-mx)