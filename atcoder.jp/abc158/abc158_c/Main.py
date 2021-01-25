a,b=map(int,input().split())
import math
for i in range(10000):
  if int(math.floor(i*0.08))==a and int(math.floor(i*0.1))==b:
    print(i)
    exit()
print(-1)
  