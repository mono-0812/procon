ans=1
n=int(input())
import math
for i in range(2,n+1):
    ans=ans*i // math.gcd(ans,i)
print(ans+1)