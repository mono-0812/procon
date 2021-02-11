n=int(input())
s=input()
mx=0
x=0
for i in s:
    if i=="I":
        x+=1
    else:
        x-=1
    mx=max(mx,x)
print(mx)