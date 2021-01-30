import itertools
n=int(input())
li=[]
for _ in range(n):
  li.append(input())
for i in itertools.combinations(li,3):
  x1,y1=map(int,i[0].split())
  x2,y2=map(int,i[1].split())
  x3,y3=map(int,i[2].split())
  if x1==x2==x3 or y1==y2==y3:
    print("Yes")
    exit()
  if x2-x1==0 or x3-x1 == 0:
    continue
  a1=(y2-y1)/(x2-x1)
  a2=(y3-y1)/(x3-x1)
  if a1!=a2:
    continue
  if a1*(x2-x1)==0 or a2*(x3-x1) == 0:
    continue
  b1=(y2-y1)/(a1*(x2-x1))
  b2=(y3-y1)/(a2*(x3-x1))
  if a1==a2 and b1==b2:
    print("Yes")
    exit()
print("No")
