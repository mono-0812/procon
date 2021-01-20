r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
mr = r2-r1
mc = c2-c1
a = r1-c1
b = r2-c2
d = r1+c1
e = r2+c2
if r1 == r2 and c1 == c2:
  print(0)
  exit()
if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <=3:
  print(1)
  exit()
if mr %2 ==0 and mc%2 ==0 or abs(d-e) <= 3 or abs(r1-r2) + abs(c1-c2) <=6 or mr %2 ==1 and mc%2 ==1 or abs(a-b)<=3:
  print(2)
  exit()
print(3)