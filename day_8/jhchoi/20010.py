# 악덕 영주 혜유
# https://www.acmicpc.net/problem/20010

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

edges = []

parent, rank = dict(), dict()

def make_set(node):
    parent[node] = node
    rank[node] = 0

[make_set(node) for node in range(0, N)]

for _ in range(K): 
    node_a, node_b, weight = map(int, input().split())
    edges.append((weight, node_a, node_b))

def union(node_a, node_b):
    root_a, root_b = find(node_a), find(node_b)
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else: 
        parent[root_a] = root_b
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
            
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

mst_node_list = [[] for _ in range(N)]
    
def kruskal(edges):
    global mst_node_list
    min_weight = 0
    for edge in edges:
        weight, node_a, node_b = edge
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            min_weight += weight
            mst_node_list[node_a].append((node_b, weight))
            mst_node_list[node_b].append((node_a, weight))
    return min_weight 

print(kruskal(sorted(edges)))

def bfs(start, max_weight):
    visited = [False] * N
    need_visit = deque([(start, 0)])
    visited[start] = True
    while need_visit:
        curr_node, curr_weight = need_visit.pop()
        max_weight = curr_weight if max_weight < curr_weight else max_weight
                    
        for next_node, next_weight in mst_node_list[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                need_visit.appendleft((next_node, curr_weight+next_weight))
    return max_weight


max_weight = 0
for start in range(N):
    max_weight = max(max_weight, bfs(start, max_weight))

print(max_weight)