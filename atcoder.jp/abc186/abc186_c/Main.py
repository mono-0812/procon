def eightval(val):
  return format(val,"o")
n = int(input())
ans = 0
for i in range(1,n+1):
  if "7" in str(i):
    ans+=1
    continue
  if "7" in str(eightval(i)):
    ans+=1
    continue
  
print(n-ans)
    

  