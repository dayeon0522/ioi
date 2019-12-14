"""
ID: tiny6571
LANG: PYTHON3
TASK: backforth
"""
fin = open('backforth.in', 'r')
fout = open('backforth.out', 'w')
in0, in1, ans, num = [int(i) for i in fin.readline().split()], [int(i) for i in fin.readline().split()], set(), 1000
for i in in0:
    in2 = in1[:]
    in2.append(i)
    num -= i
    for j in in2:
        num += j
        in3 = in0[:]
        in3.remove(i)
        in3.append(j)
        for k in in3:
            num -= k
            in4 = in1[:]
            in4.append(i)
            in4.append(k)
            in4.remove(j)
            for l in in4:
                num += l
                ans.add(num)
                num -= l
            num += k
        num -= j
    num += i
fout.write(str(len(ans)))
fout.close()