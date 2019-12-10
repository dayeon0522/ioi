"""
ID: tiny6571
LANG: PYTHON3
TASK: herding
"""
fin = open('herding.in', 'r')
fout = open('herding.out', 'w')
list = [int(i) for i in fin.readline().split()]
max = max(list[1] - list[0], list[2] - list[1])
if list[0] + 1 == list[1] and list[1] + 1 == list[2]:
    fout.write('0\n')
elif list[1] - list[0] == 2 or list[2] - list[1] == 2:
    fout.write('1\n')
else:
    fout.write('2\n')
fout.write(str(max - 1) + '\n')
fout.close()