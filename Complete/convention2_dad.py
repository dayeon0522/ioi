"""
ID: tiny6571
LANG: PYTHON3
TASK: convention2
"""
import heapq

fin = open('convention2.in', 'r')
fout = open('convention2.out', 'w')
n, list = int(fin.readline()), []

heap, heap2 = [], []

for i in range(n):
    list.append([int(i) for i in fin.readline().split()])
    list[-1].append(i)
    heapq.heappush(heap, (list[-1][0], i, list[-1]))


num, waiting = 0, 0
for i in range(n):
    while True:
        pop = heapq.heappop(heap)[2]

        if num < pop[0] or not heap:
            if heap2:
                heapq.heappush(heap, (pop[0], pop[2], pop))
                pop = heapq.heappop(heap2)[2]

            if num < pop[0]:
                num = pop[0]
            waiting = max(num - pop[0], waiting)
            num += pop[1]
            break
        else:
            heapq.heappush(heap2, (pop[2], pop[0], pop))


fout.write(str(waiting))
fout.close()