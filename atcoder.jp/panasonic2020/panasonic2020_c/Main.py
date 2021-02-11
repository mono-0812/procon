import decimal
a,b,c=map(decimal.Decimal,input().split())
pf=decimal.Decimal(0.5)
if a**pf + b**pf < c**pf:
    print("Yes")
    exit()
print("No")
