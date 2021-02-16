n=int(input())
val=1000-n
li=[1,5,10,50,100,500,1000]
li.reverse()
cnt=0
for i in range(7):
    while val >= li[i]:
        cnt+=1
        val-=li[i]
    if val==0:
        break
print(cnt)