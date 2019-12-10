"""
ID: tiny6571
LANG: PYTHON3
TASK: mixmilk
"""
fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')
a = fin.readline()
b = fin.readline()
c = fin.readline()

nums = []
a = [int(x) for x in a.split() ]
b = [int(x) for x in b.split() ]
c = [int(x) for x in c.split() ]
nums.extend([a, b, c])
print(nums)
for i in range(100):
    temp = i % 3
    next = (i + 1) % 3
    diff = nums[next][0] - nums[next][1]
    if nums[temp][1] <= diff:
        nums[next][1] += nums[temp][1]
        nums[temp][1] = 0
    else:
        nums[next][1] = nums[next][0]
        nums[temp][1] -= diff
fout.write(str(nums[0][1]) + '\n')
fout.write(str(nums[1][1]) + '\n')
fout.write(str(nums[2][1]) + '\n')
fout.close()