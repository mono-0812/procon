import math
import itertools
k = int(input())
ans=0
for i in itertools.combinations_with_replacement(list(range(1,k+1)),3):
    val=math.gcd(i[2],math.gcd(i[0],i[1]))
    if len(set(i)) ==1:
        ans+=val
        continue
    elif len(set(i)) == 2:
        val*=3
        ans+=val
        continue
    else:
        val*=6
        ans+=val
        continue

print(ans)
