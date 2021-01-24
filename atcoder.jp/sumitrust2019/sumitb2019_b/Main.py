n=int(input())
x=int(n//1.08+1)
if int(x*1.08) == n:
  print(x)
  exit()
print(":(")