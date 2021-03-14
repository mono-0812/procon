a,b,w=map(int,input().split())
w*=1000
val=w//b
val2=w//a+1
mi=10**15
mx=10**-15
for i in range(val,val2+1):
    if a<=w/i<=b:
        mi=min(mi,i)
        mx=max(mx,i)
if mi==10**15 and mx==10**-15:
    print("UNSATISFIABLE")
    exit()
print(mi,mx)
