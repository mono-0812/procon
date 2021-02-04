import collections
n=int(input())
a_list=list(map(int,input().split()))
c=collections.Counter(a_list)
c_set = set(a_list)
check=-1
check_list=[]
if len(c)==1:
    if c[0]!=0:
        print("Yes")
        exit()
elif len(c)==2:
    if c[0] == n//3:
        print("Yes")
        exit()
elif len(c)==3:
    for i in c_set:
        check_list.append(i)
        if check == -1:
            check = c[i]
        else:
            if check != c[i]:
                print("No")
                exit()
    else:
        res = check_list[0] ^ check_list[1] ^ check_list[2]
        if res == 0:
            print("Yes")
            exit()
print("No")