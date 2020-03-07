"""
ID: tiny6571
LANG: PYTHON3
TASK: lineup
"""
fin = open('lineup.in', 'r')
fout = open('../lineup.out', 'w')
perfect = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
check = int(fin.readline())
list = []
for i in range(check):
    v = fin.readline().split()
    list.append([perfect.index(v[-1]), perfect.index(v[0])])
def recur(visit, count, nums):
    if count == 8:
        for i in list:
            if nums.index(i[0]) - 1 != nums.index(i[1]) and nums.index(i[0]) + 1 != nums.index(i[1]):
                break
        else:
            for i in nums:
                fout.write(perfect[i] + '\n')
            fout.close()
            return True
        return False
    for i in range(8):
        if visit[i] == False:
            visit[i] = True
            nums.append(i)
            re = recur(visit, count + 1, nums)
            if re:
                return True
            visit[i] = False
            nums.pop()
recur([False] * 8, 0, [])