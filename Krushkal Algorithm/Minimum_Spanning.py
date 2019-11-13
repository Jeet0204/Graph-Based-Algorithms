from collections import defaultdict
import heapq
def minimum_spanning(graph, start_node):
    mst = defaultdict(set)
    
    totalcost = 0
    visited = set([start_node])
    edges = [(cost, start_node, to)for to, cost in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            totalcost += int(cost)
            print('Path cost from '+str(frm)+' To '+str(to)+' : '+str(cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next)) 
    print("Total cost: ",totalcost)
    return mst