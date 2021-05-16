y=int(input())
if (not y%100==0 and y%4==0) or y%400==0:
    print("YES")
else:
    print("NO")