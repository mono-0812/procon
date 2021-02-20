n=int(input())
S=[]
for _ in range(n):
    S.append("".join(sorted(input())))
import collections
import math
SC=collections.Counter(S)
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans=0
for i in SC.keys():
    if SC[i] >= 2:
        ans+=combinations_count(SC[i],2)
print(ans)