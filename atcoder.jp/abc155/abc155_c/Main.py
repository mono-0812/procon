n=int(input())
S=[]
for _ in range(n):S.append(input())
import collections
sc=collections.Counter(S)
mxval=max(sc.values())
ans=[]
for key,val in sc.items():
    if val == mxval:
        ans.append(key)
ans.sort()
for i in ans:
    print(i)
