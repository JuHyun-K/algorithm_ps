import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)

'''
minHeap이니까, push, pop할 때 -1을 곱해야함
'''



