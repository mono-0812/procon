a,b,h,m=map(int,input().split())
deg=(h*60+m)*5.5%360
if deg>180:
    deg=360-deg
import math
ans2=(a**2+b**2-2*a*b*math.cos(math.radians(deg)))
print(ans2**0.5)