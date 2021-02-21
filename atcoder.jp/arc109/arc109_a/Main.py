a,b,x,y=map(int,input().split())
if a<=b:
    print(x+min(y,2*x)*(b-a))
else:
    print(x+min(y,2*x)*(a-b-1))