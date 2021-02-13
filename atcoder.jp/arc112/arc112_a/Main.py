t=int(input())
for i in range(t):
    total=0
    l,b=map(int,input().split())
    if l==b and l>0:
        print(0)
        continue
    if l*2 > b:
        print(0)
        continue
    print((b-2*l+1)*(b-2*l+2)//2)
total=0
