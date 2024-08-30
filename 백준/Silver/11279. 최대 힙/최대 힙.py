import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) > 0:
            print(-1 * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -1 * x)