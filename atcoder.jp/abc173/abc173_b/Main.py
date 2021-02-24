n=int(input())
import collections
S=[]
for i in range(n):
    S.append(input())
S=collections.Counter(S)
print("AC x",S["AC"])
print("WA x",S["WA"])
print("TLE x",S["TLE"])
print("RE x",S["RE"])
