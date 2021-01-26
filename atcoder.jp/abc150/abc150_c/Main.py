import itertools
n=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
li=[]
s=""
cnt=1
for i in P:
  s+=str(i)
p=int(s)
s=""
for i in Q:
  s+=str(i)
q=int(s)
s=""
for i in list(itertools.permutations(Q)):
  for m in i:
    s+=str(m)
  li.append(int(s))
  s=""
li.sort()
for i in li:
  if i == p:
    a = cnt
  if i == q:
    b = cnt
  cnt+=1
print(abs(a-b))
  