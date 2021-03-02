s=input()
las=""
for i in s:
    if las==i:
        print("Bad")
        exit()
    las=i
print("Good")