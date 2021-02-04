n=int(input())
s=input()
las=""
for i in s:
    if las == i:
        n-=1
    else:
        las=i
print(n)