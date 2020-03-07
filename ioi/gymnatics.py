"""
ID: tiny6571
LANG: PYTHON3
TASK: gymnastics
"""
fin = open('gymnastics.in', 'r')
fout = open('gymnastics.out', 'w')
data, ans = [], 0
k, n = fin.readline().split()
k, n = int(k), int(n)
for i in range(k):
    index = 0
    dict = {}
    for j in fin.readline().split():
        dict[int(j)] = index
        index += 1
    data.append(dict)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue
        for dict in data:
            if dict[i] > dict[j]:
                break
        else:
            ans += 1
fout.write(str(ans))
fout.close()

