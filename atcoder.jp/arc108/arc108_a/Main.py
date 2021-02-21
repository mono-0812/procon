s,p=map(int,input().split())
for i in range(1,int(p**0.5)+1):
    if i*(s-i)==p:
        print("Yes")
        exit()
print("No")