n,m=map(int,input().split())
import math
ans=math.floor(pow(10,n,m**2)/m)%m
print(ans)