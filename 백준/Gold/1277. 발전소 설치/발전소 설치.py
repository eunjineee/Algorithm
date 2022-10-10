# from pprint import pprint
import heapq
import sys
input = sys.stdin.readline

def f(start):
    q = []
    heapq.heappush(q,(start, 0))
    visited[start] = 0
    while q:
        now, time = heapq.heappop(q)
        if visited[now] < time:
            continue
        if now in wiredi.keys() and len(wiredi[now]) != 0:
            for (node, node_time) in wiredi[now]:
                next_time = time + node_time
                if next_time < visited[node]:
                    visited[node] = next_time
                    heapq.heappush(q, (node, next_time))

plant, wire = map(int,input().split())
minwire = float(input().rstrip())

plantdi = {}
for i in range(1, plant+1):
    x, y = map(int,input().split())
    plantdi[i] = (x,y)
# print(f'plantdi:')
# pprint(plantdi)

wiredi = {}
for j in range(1, plant+1):
    wiredi[j] = []

for _ in range(wire):
    a, b = map(int, input().split())
    wiredi[a].append((b,0))
    wiredi[b].append((a,0))
# print(f'wiredi:')
# pprint(wiredi)

for aa in range(1,plant+1):
    for bb in range(aa+1,plant+1):
        wirelen = (abs(plantdi[bb][0]-plantdi[aa][0])**2 + abs(plantdi[bb][1]-plantdi[aa][1])**2 )**(0.5)
        if wirelen <= minwire:
                wiredi[aa].append((bb, wirelen))
                wiredi[bb].append((aa, wirelen))
# print(f'wiredi:')
# pprint(wiredi)

INF = sys.maxsize
visited = [INF] * (plant + 1)

f(1)

# pprint(visited)
print(int(visited[plant] * 1000))