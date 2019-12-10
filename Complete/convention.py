"""
ID: tiny6571
LANG: PYTHON3
TASK: convention
"""
fin = open('convention2.in', 'r')
fout = open('convention.out', 'w')
list = [int(i) for i in fin.readline().split()]
cows, bus, hold = list[0], list[1], list[2]
list = [int(i) for i in fin.readline().split()]
list.sort()

def while_true(mid):
    index = 0
    for i in range(bus):
        for j in range(1, hold):
            if index + j >= len(list):
                return True
            if list[index + j] - list[index] > mid:
                index += j
                break
        else:
            index += j + 1
        if index >= len(list):
            return True
    return False


def check(left, right):
    if left >= right:
        return left
    mid = int((left + right)/2)
    ans = while_true(mid)
    if ans:
        return check(left, mid)
    else:
        return check(mid + 1, right)

fout.write(str(check(0, 10 ** 9)))
fout.close()