"""
ID: tiny6571
LANG: PYTHON3
TASK: whereami
"""
fin = open('whereami.in', 'r')
fout = open('whereami.out', 'w')
n = int(fin.readline())
string = fin.readline()
for i in range(1, n + 1):
    sett = set()
    for j in range(len(string) - i + 1):
        if string[j:j + i] not in sett:
            sett.add(string[j:j + i])
        else:
            break
    else:
        fout.write(str(i))
        break
fout.close()