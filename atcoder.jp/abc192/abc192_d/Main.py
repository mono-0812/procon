X=input()
M=int(input())
d=int(max(X))
if len(X)==1:
    if int(X) > M:
        print(0)
    else:
        print(1)
    exit()
def f(d):
    num = 0
    for x in X:
        num = num*d + int(x)
    return num > M
l,r = d,M+1
while l+1 < r:
    m=(l+r)//2
    if f(m):
        r=m
    else:
        l=m
print(l-d)
