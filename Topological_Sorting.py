def topological_sort(graph):
    visited = set()
    topo_order = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
        topo_order.append(vertex)  # Add after visiting neighbors

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return topo_order[::-1]  # Reverse to get correct topological order

# Example usage:
# Graph is represented as an adjacency list where graph[u] = [v1, v2, ...]
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print("Topological Sort:", topological_sort(graph))
