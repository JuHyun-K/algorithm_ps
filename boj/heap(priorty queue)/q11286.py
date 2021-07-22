import sys
import heapq

input = sys.stdin.readline
heap = []
n = int(input())

for _ in range(n):
    # print(heap)
    x = int(input())
    if x == 0:
        if heap:
            val = heapq.heappop(heap)
            if not val[1]:
                val[0] *= -1
            print(val[0])

        else:
            print(0)
    else:
        if x > 0:
            heapq.heappush(heap, [x, True])
        else:
            heapq.heappush(heap, [-x, False])

# false가 true보다 먼저 출력됨