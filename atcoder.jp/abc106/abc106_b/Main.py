n=int(input())
cnt=0
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
for i in range(1,n+1):
    a=make_divisors(i)
    if len(a)==8:
        if i%2==1:
            cnt+=1
print(cnt)
