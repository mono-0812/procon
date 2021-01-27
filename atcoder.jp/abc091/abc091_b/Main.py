n=int(input())
S=[]
T=[]
plus=0
minus=0
mx=0
word=""
for i in range(n):
  s=input()
  S.append(s)
m=int(input())
for i in range(m):
  t=input()
  T.append(t)
for i in S:
  plus=S.count(i)
  minus=T.count(i)
  if mx < plus-minus:
    mx=plus-minus
print(mx)

