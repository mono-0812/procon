n=int(input())
sn=int(n**0.5)
li=[]
for i in range(2,sn+1):
    cnt=2
    while n>= i**cnt:
        li.append(i**cnt)
        cnt+=1
li=set(li)
print(n-len(li))