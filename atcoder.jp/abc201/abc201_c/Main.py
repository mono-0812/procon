s=input()
maru,batu=set(),set()
for i in range(len(s)):
    if s[i]=="o":
        maru.add(str(i))
    elif s[i]=="x":
        batu.add(str(i))
ans=0
for i in range(10000):
    num=str(i).rjust(4,"0")
    if maru <= set(list(num)) and len(set(list(num))) == len(set(list(num))-batu):
        ans+=1
print(ans)
