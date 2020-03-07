"""
ID: tiny6571
LANG: PYTHON3
TASK: moobuzz
"""
fin = open('swap.in', 'r')
fout = open('a.out', 'w')
n = int(fin.readline())
def fn(num):
    return num - (int(num / 3) + int(num / 5) - int(num / 15))
def bs(l, r, num):
    m = int((l + r) / 2)
    if fn(m) == num:
        return m
    if fn(m) > num:
        return bs(l, m - 1, num)
    else:
        return bs(m + 1, r, num)
num = 0
a = bs(1, 10 ** 10, n)
while True:
    if (a - num) % 3 != 0 and (a - num) % 5 != 0:
        fout.write (str(a - num))
        break
    num += 1
fout.close()