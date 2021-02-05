n=int(input())
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
div=make_divisors(n)
ans=0
for i in div:
    if (i+(2*n//i))%2==1:
        ans+=1
print(ans*2)