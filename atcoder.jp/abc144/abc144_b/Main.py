n = int(input())
count = 0
for a in range(1,10):
  for b in range(1,10):
    if a*b==n:
      count+=1
if count == 0:
  print("No")
else:
  print("Yes")