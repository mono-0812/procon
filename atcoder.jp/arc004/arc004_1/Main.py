import math
def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d
n = int(input())
mx = 0
xy =[]
for i in range(n):
  x,y = map(int,input().split())
  xy.append(str(x)+" "+str(y))
for i in xy:
  x,y = map(int,i.split())
  for s in xy:
    x2,y2 = map(int,s.split())
    mx = max(mx,get_distance(x,y,x2,y2))
print(mx)