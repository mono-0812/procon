n = int(input())
li=[]

for i in range(n):
    li.append(int(input()))
li2=sorted(li,reverse=True)
for i in li:
    if li2[0]!=i:
        print(li2[0])
    else:
        print(li2[1])
