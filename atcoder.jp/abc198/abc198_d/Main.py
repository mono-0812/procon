import bisect,collections,copy,heapq,itertools,math,string,sys
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int,input().split())
def LIIS(): return list(map(int,input().split()))
INF=float("inf")
MOD=10**9+7
##############################################################################
s1=I();s2=I();s3=I()
li=list(set(s1+s2+s3))
if len(li)>=11:
    print("UNSOLVABLE")
    exit()
t=0
for l in itertools.permutations(range(10),len(li)):
    dic={}
    S1=0
    S2=0
    S3=0
    i=0
    for key in li:
        dic[key]=l[i]
        i+=1
    if dic[s1[0]]==0 or dic[s2[0]]==0 or dic[s3[0]]==0:continue
    for i in range(len(s1)):
        S1=S1*10+dic[s1[i]]
    for i in range(len(s2)):
        S2=S2*10+dic[s2[i]]
    for i in range(len(s3)):
        S3=S3*10+dic[s3[i]]
    if S1+S2==S3:
        print(S1)
        print(S2)
        print(S3)
        exit()
print("UNSOLVABLE")


