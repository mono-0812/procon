n=int(input())
s=input()
print("YNeos"[s.count("B")>=s.count("R")::2])