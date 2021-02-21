k=int(input())
#makemakeが元の数だよ
def make_divisors(makemake):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= makemake:
        if makemake % i == 0:
            lower_divisors.append(i)
            if i != makemake // i:
                upper_divisors.append(makemake//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
ans=0
li=[[]]*(k*2)
for i in range(1,k+1):
    li[i]=make_divisors(i)
for i in range(1,k+1):
    for j in li[i]:
        ans+=len(li[j])
print(ans)