a,b,c,d=map(int,input().split())
import math
cd=(c*d)// math.gcd(c,d)
k=b-a+1
print(k-(b//c-(a-1)//c)-(b//d-(a-1)//d)+(b//cd-(a-1)//cd))