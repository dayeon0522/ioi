"""
ID: tiny6571
LANG: PYTHON3
TASK: swap
"""
fin = open('swap.in', 'r')
fout = open('swap.out', 'w')
n, m, k = [int(i) for i in fin.readline().split()]
list = []
list2 = [j + 1 for j in range(n)]
ans = [0] * n
dict = {}
for j in range(m):
    list.append([int(j) for j in fin.readline().split()])
for nums in list:
    list2[nums[0] - 1:nums[1]] = list2[nums[0] - 1:nums[1]][::-1]
for j in range(n):
    dict[list2[j]] = j + 1

path = {}
for j in range(n):
    if j+1 not in path:
        count = 1
        cur = dict[j + 1]
        memo = [j + 1]
        while cur != j + 1:
            count += 1
            memo.append(cur)
            cur = dict[cur]
        for i in range(len(memo)):
            path[memo[i]] = (memo, i)

for j in range(n):
    l, index = path[j + 1]
    ans[l[(k % len(l) + index) % len(l)] - 1] = j + 1
for j in ans:
    fout.write(str(j) + '\n')
fout.close()