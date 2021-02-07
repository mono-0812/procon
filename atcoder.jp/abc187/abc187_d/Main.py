n=int(input())
X=0
x=[]
for i in range(n):
    a,b=map(int,input().split())
    X-=a
    x.append(2*a+b)
x.sort()
c=0
while X<=0:
    X+=x.pop()
    c+=1
print(c)
