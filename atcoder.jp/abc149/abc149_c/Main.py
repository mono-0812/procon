x=int(input())
flag=True
cnt=0
while flag:
    for i in range(2,int(x**0.5)):
        if x%i!=0:
            continue
        cnt=1
        break
    if cnt==0:
        print(x)
        exit()
    cnt=0
    x+=1