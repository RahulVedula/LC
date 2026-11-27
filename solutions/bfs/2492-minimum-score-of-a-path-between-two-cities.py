from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for a, b, distance in roads:
            adj[a].append((b, distance))
            adj[b].append((a, distance))
        
        queue = deque([1])
        visited = {1}
        min_score = float("inf")
        
        while queue:
            node = queue.popleft()
            
            for adj_node, distance in adj[node]:
                min_score = min(min_score, distance)
                
                if adj_node not in visited:
                    visited.add(adj_node)
                    queue.append(adj_node)
                    
        return min_score