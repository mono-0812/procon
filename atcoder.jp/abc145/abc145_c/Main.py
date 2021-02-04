n=int(input())
X=[]
Y=[]
total=0
def dif(x,y,x2,y2):
    return ((x-x2)**2+(y-y2)**2)**0.5
for _ in range(n):
    a,b=map(int,input().split())
    X.append(a)
    Y.append(b)
import itertools
for i in itertools.permutations(list(range(n)),n):
    for j in range(n-1):
        total+=dif(X[i[j]],Y[i[j]],X[i[j+1]],Y[i[j+1]])
import math
print(total / math.factorial(n))