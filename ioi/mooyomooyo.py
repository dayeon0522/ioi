"""
ID: tiny6571
LANG: PYTHON3
TASK: mooyo
"""
def find(q, l):
    for nums in q:
        y, x = nums[0], nums[1]
        if x - 1 != -1 and l[y][x - 1] == l[y][x] and (y, x - 1) not in q:
            q.append((y, x - 1))
        if x + 1 != len(l[y]) and l[y][x + 1] == l[y][x] and (y, x + 1) not in q:
            q.append((y, x + 1))
        if y - 1 != -1 and l[y - 1][x] == l[y][x] and (y - 1, x) not in q:
            q.append((y - 1, x))
        if y + 1 != len(l) and l[y + 1][x] == l[y][x] and (y + 1, x) not in q:
            q.append((y + 1, x))

def delete(q, l):
    while q:
        y, x = q.pop()
        l[y][x] = 0

def drop(l):
    flag = False
    for i in range(10):
        for j in range(len(l) - 2, -1, -1):
            if l[j][i] == 0:
                continue
            for k in range(0, len(l) - j - 1):
                if l[j + 1 + k][i] == 0:
                    l[j + 1 + k][i], l[j + k][i] = l[j + k][i], l[j + 1 + k][i]
                    flag = True
    return flag

fin = open('mooyomooyo.in', 'r')
fout = open('mooyomooyo.out', 'w')
n, list, queue, flag = [int(i) for i in fin.readline().split()], [], [], True
for i in range(n[0]):
    list.append([int(j) for j in fin.readline() if j != '\n'])
while True:
    flag = True
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j]:
                queue.append((i, j))
                find(queue, list)
                if len(queue) >= n[1]:
                    delete(queue, list)
                    flag = False
                else:
                    queue = []
    if flag or not drop(list):
        break
for i in list:
    fout.write("".join([str(j) for j in i]) + '\n')
fout.close()