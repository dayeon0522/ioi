"""
ID: tiny6571
LANG: PYTHON3
TASK: shell
"""
fin = open('shell.in', 'r')
fout = open('shell.out', 'w')
n = int(fin.readline())
list, n123, n1, n2, n3 = [], [1, 2, 3], 0, 0, 0
for i in range(n):
    list.append([int(j) for j in fin.readline().split()])
for nums in list:
    step1, step2 = nums[0], nums[1]
    n123[step1 - 1], n123[step2 - 1] = n123[step2 - 1], n123[step1 - 1]
    if n123[nums[2] - 1] == 1:
        n1 += 1
    elif n123[nums[2] - 1] == 2:
        n2 += 1
    else:
        n3 += 1
fout.write(str(max(n1, n2, n3)))
fout.close()