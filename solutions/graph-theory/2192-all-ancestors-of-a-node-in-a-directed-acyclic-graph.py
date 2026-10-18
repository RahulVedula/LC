class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # Topological sort
        adj = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        queue = deque([node for node, deg in enumerate(in_degree) if deg == 0])
        ancestors = [set() for _ in range(n)]

        while queue:
            node = queue.popleft()

            for next_node in adj[node]:
                in_degree[next_node] -= 1
                ancestors[next_node].add(node)
                ancestors[next_node] = ancestors[next_node] | ancestors[node]
                if in_degree[next_node] == 0:
                    queue.append(next_node)
        
        return [sorted(list(ancestor)) for ancestor in ancestors]
