n=int(input())
li=list(map(int,input().split()))
li.sort()
li1=li[:len(li)//2]
li2=li[len(li)//2:]
print(len(list(range(li1[-1]+1,li2[0]+1))))
