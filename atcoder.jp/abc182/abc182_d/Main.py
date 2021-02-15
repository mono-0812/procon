import itertools
n=int(input())
A=list(map(int,input().split()))
S=list(itertools.accumulate(A))
X=[0] + list(itertools.accumulate(S))
V=list(itertools.accumulate(S,func=max))
ans=max(X[i]+V[i] for i in range(n))
print(max(0,ans))