from scipy.special import comb
l = int(input())
print(comb(l-1,11,exact=True))