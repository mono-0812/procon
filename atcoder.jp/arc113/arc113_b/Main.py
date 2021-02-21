a,b,c=map(int,input().split())
al=[1,5,6]
two=[4,9]
four=[2,3,8,7]
one=int(str(a)[-1])
val=0
if one in al:
    print(one)
    exit()
if one in two:
    val=False
if one in four:
    val=True
if val:
    if pow(b,c,4)%4==0:
        print(str(a**4)[-1])
        exit()
    print(str(a**(pow(b,c,4)%4))[-1])
    exit()
else:
    if pow(b,c,2)%2==0:
        print(str(a**2)[-1])
        exit()
    print(str(a**(pow(b,c,2)%2))[-1])
    exit()