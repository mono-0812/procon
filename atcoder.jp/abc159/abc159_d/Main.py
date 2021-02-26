n=int(input())
A=list(map(int,input().split()))
import collections
import math
Ac=collections.Counter(A)
ans=0
for i in Ac.keys():
    ans+=(Ac[i]*(Ac[i]-1)//2)
li=[0]
for i in range(1,10**5*3):
    li.append((i*(i-1))//2)
for i in A:
    print(ans-li[Ac[i]]+li[Ac[i]-1])


    
