a,b=map(int,input().split())
s=""
if a<b:
    for i in range(b):
        s+=str(a)
    print(s)
    exit()
elif b<a:
    for i in range(a):
        s+=str(b)
    print(s)
    exit()
else:
    for i in range(max(a,b)):
        s+=str(a)
    print(s)
