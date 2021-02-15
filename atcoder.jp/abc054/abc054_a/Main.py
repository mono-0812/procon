a,b=map(int,input().split())
if a==b:
    print("Draw")
    exit()
if a>b and b!=1 or a==1:
    print("Alice")
else:
    print("Bob")