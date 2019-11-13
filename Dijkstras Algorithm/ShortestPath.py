import collections
import heapq


def shortestpath(edges, source, goal, g):
    graph = collections.defaultdict(set)

    if g == 'D':
        for left,right,cost in edges:
            graph[left].add((cost, right))
            
            
    else:
        for left,right,cost in edges:
            graph[left].add((cost, right))
            graph[right].add((cost, left))
            
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return (cost, path)
            for c, neighbour in graph[node]:
                
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+int(c), neighbour, path))
    return float("inf")

