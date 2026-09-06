class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        label_map = defaultdict(dict)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def getFreq(root, prev):
            root_map = defaultdict(int)
            label = labels[root]
            root_map[label] += 1

            for neighbour in adj[root]:
                if neighbour == prev:
                    continue

                next_map = getFreq(neighbour, root)

                for key, freq in next_map.items():
                    root_map[key] += freq

            label_map[root] = root_map
            return label_map[root]

        getFreq(0,-1)
        labelled = [0] * n
        for node in range(n):
            label = labels[node]
            labelled[node] = label_map[node][label]
            
        return labelled
