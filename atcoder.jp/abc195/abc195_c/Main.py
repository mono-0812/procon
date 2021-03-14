n=int(input())
val=len(str(n))
ans=0
for i in range(val-1):
    cm=i//3
    vl=10**(i+1)-1
    vl2=10**(i)-1
    ans+=(vl-vl2)*cm
i=val-1
cm=i//3
vl2=10**(i)-1
print(ans+(n-vl2)*cm)
