k = int(input())
seven=0
for i in range(1,10**7):
  seven*=10
  seven+=7
  seven %= k
  if seven == 0:
    print(i)
    exit()
print(-1)