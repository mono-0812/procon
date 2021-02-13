#n=int(input())
v,t,s,d=map(int,input().split())
#li=list(map(int,input().split()))
if t<=d/v<=s:
    print("No")
else:
    print("Yes")