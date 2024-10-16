import heapq

def prims_algorithm(graph, start_vertex):
    # Initialize min heap
    min_heap = [(0, start_vertex)]
    visited = set()
    total_cost = 0
    mst_edges = []

    while min_heap:
        # Get the edge with minimum weight
        weight, current_vertex = heapq.heappop(min_heap)

        # If the vertex is already visited, skip it
        if current_vertex in visited:
            continue

        # Mark the vertex as visited
        visited.add(current_vertex)
        total_cost += weight

        # If not the first vertex, add the edge to the MST
        if weight != 0:
            mst_edges.append((current_vertex, weight))

        # Add all the neighbors of the current vertex to the heap
        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst_edges, total_cost

# Example graph representation: adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

# Run Prim's algorithm
mst_edges, minimum_cost = prims_algorithm(graph, 'A')
print(f"Minimum Spanning Tree Edges: {mst_edges}; Total Cost: {minimum_cost}")
