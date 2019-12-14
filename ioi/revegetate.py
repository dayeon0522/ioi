"""
ID: tiny6571
LANG: PYTHON3
TASK: revegetate
"""
def match(set1, set2):
    for num in set1:
        if num in set2:
            return True
    return False
fin = open('mooyomooyo.in', 'r')
fout = open('revegetate.out', 'w')
n, list, s = [int(i) for i in fin.readline().split()], [], ''
save, nums = [set(), set(), set(), set()], [set() for _ in range(n[0])]
for i in range(n[1]):
    list.append([int(j) for j in fin.readline().split()])
for i in range(len(list)):
    nums[list[i][0] - 1].add(i + 1)
    nums[list[i][1] - 1].add(i + 1)
for i in range(len(nums)):
    for j in range(len(save)):
        if not match(nums[i], save[j]):
            save[j].add(k for k in nums[i])
            save[j].update(nums[i])
            s += str(j + 1)
            break
fout.write(s)
fout.close()