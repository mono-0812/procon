n,w = map(int,input().split())
count = 0
weight = w
while n >= weight:
  weight += w
  count += 1
print(count)