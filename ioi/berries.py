"""
ID: tiny6571
LANG: PYTHON3
TASK: berries
"""
fin = open('swap.in', 'r')
fout = open('swap.out', 'w')
n, k = fin.readline().split()
n, k = int(n), int(k)
list = [int(i) for i in fin.readline().split()]
list.sort()
list = list[-k:]
m = 0
def recur(list, divide):
    global m, k
    list1 = list[:]
    if list1[-1] // divide >= list1[0]:
        n = list1.pop()
        list1.extend([(n // divide) + 1] * (n % divide) + [(n // divide)] * (divide - (n % divide)))
        list1.sort()
        list1 = list1[len(list1) - k:]
        m = max(m, sum(list1[:k // 2]))
    else:
        m = max(m, sum(list[:k // 2]))
        return True
    for i in range(2, k + 1):
        if recur(list1, i):
            break
    return False
for i in range(2, k + 1):
    recur(list, i)
fout.write(str(m))
fout.close()