n=int(input())
li=list(map(int,input().split()))
man=0
you=0
che=0
cheli=[]
for i in li:
  man+=abs(i)
  you+=abs(i)**2
  cheli.append(abs(i))
print(man)
print(you**0.5)
print(max(cheli))