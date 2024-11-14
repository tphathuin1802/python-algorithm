with open(
    "C:/Local Code/Tutorial&Learning/MainLanguages/Python/Algorithm/Euclid/UCLN.INP"
) as fi:
    m, n = map(int, fi.readline().split())


def gcd_ab(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


output_gcd = gcd_ab(m, n)

with open(
    "C:/Local Code/Tutorial&Learning/MainLanguages/Python/Algorithm/Euclid/UCLN.INP",
    "w",
) as fo:
    fo.write(str(output_gcd))
