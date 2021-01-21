n = int(input())
val = 0
for i in range(1,n+1):
  val += i
for i in range(2,val//2):
  if val%i == 0:
    print("BOWWOW")
    exit()
if val == 1:
  print("BOWWOW")
  exit()
print("WANWAN")