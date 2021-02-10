h,w,k=map(int,input().split())
field=[]
ans=0
for _ in range(h): field.append(list("".join(input())))
import copy
kc=copy.deepcopy(k)
for i in range(2 ** (h+w)):
    fieldcopy=copy.deepcopy(field)
    cnt=0
    for j in range(h+w):
        if ((i >> j) & 1):
            if j<h:
                fieldcopy[j]=["r"]*w
            else:
                for k in range(h):
                    fieldcopy[k][j-h]="r"
    
    for j in fieldcopy:
        cnt+=j.count("#")
        
    k=kc
    if cnt==k:
        ans+=1
print(ans)