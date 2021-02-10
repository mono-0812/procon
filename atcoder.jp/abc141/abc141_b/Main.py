s=input()
odd=["R","U","D"]
even=["L","U","D"]
for i in range(len(s)):
    if i%2==1:
        if s[i] not in even:
            print("No")
            exit()
    else:
        if s[i] not in odd:
            print("No")
            exit()
print("Yes")

