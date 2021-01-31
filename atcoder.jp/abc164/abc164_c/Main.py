n=int(input())
s=[]
for i in range(n):
  x=input()
  s.append(x)
s=set(s)
print(len(s))