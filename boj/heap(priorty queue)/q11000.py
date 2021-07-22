import sys
import heapq

input = sys.stdin.readline
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
times.sort()

print(times)
heap_arr = []

