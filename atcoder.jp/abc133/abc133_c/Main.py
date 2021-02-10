l,r=map(int,input().split())
mi = 2018

if r-l >=2019:
    print(0)
    exit()
else:
    for j in range(l,r+1):
        for i in range(l,r+1):
            if i>=j:
                continue
            mi=min(mi,i*j%2019)
    print(mi)