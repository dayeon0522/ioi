"""
ID: tiny6571
LANG: PYTHON3
TASK: guess
"""
fin = open('guess.in', 'r')
fout = open('guess.out', 'w')
n, list, max_yes = int(fin.readline()), [], 0
for i in range(int(n)):
    list.append(fin.readline().split())
    list[-1].pop(0)
    list[-1].pop(0)
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        yes = 0
        for k in list[i]:
            if k in list[j]:
                yes += 1
        if max_yes < yes:
            max_yes = yes
fout.write(str(max_yes + 1))
fout.close()