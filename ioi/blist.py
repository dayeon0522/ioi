"""
ID: tiny6571
LANG: PYTHON3
TASK: blist
"""
fin = open('blist.in', 'r')
fout = open('blist.out', 'w')
line = fin.readline()
input = []
for i in range(int(line)):
    input.append(fin.readline().split())
nums = [0]*1000
for list in input:
    for i in range(int(list[0]), int(list[1]) + 1):
        nums[i - 1] += int(list[2])
fout.write(str(max(nums)))
fout.close()