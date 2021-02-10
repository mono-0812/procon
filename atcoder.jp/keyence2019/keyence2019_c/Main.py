n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if sum(A)<sum(B):
    print(-1)
    exit()
cnt=0
plus=[]
minus=0
minuscnt=0
for i in range(n):
    if A[i]-B[i]>=0:
        plus.append(A[i]-B[i])
    else:
        minus+=A[i]-B[i]
        minuscnt+=1
plus.sort()
ln=len(plus)
while minus<0:
    minus+=plus.pop()
print(minuscnt+ln-len(plus))