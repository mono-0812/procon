li=list(map(int,input().split()))
import itertools
for i in range(1,5):
    for j in itertools.permutations(li,i):
        if 2*sum(j)==sum(li):
            print("Yes")
            exit()
print("No")