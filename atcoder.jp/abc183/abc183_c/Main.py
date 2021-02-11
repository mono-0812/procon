n,k=map(int,input().split())
T=[]
for i in range(n): T.append(list(map(int,input().split())))
import itertools
total=0
ans=0
for i in itertools.permutations(list(range(1,n))):
    total=0
    for j in range(n-2):
        total+=T[i[j]][i[j+1]]
    total+=T[0][i[0]]+T[i[-1]][0]
    if total==k:
        ans+=1
print(ans)