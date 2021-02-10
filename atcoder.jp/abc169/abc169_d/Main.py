n=int(input())
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
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
div=make_divisors(n)
cnt=0
for i in div:
    if len(set(prime_factorize(i)))==1 and n%i==0:
        n//=i
        cnt+=1
print(cnt)

    