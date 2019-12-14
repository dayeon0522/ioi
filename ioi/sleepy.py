"""
ID: tiny6571
LANG: PYTHON3
TASK: sleepy
"""
fin = open('sleepy.in', 'r')
fout = open('sleepy.out', 'w')
n, list, con = fin.readline(), [int(i) for i in fin.readline().split()], 0
for i in range(len(list) - 2, -1, -1):
    if list[i] <= list[i + 1]:
        con += 1
    else:
        break
fout.write(str(int(n) - con - 1))
fout.close()