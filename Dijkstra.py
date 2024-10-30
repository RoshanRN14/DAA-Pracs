import heapq

def dijkstra(graph, start):
    # Initialize the minimum distance table with infinity for all vertices
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Distance to the start vertex is zero
    priority_queue = [(0, start)]  # Priority queue to store (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If a shorter path is already found, skip this one
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
# Graph is represented as an adjacency list where graph[u] = {v: weight}
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
start_vertex = 'A'
print("Shortest distances:", dijkstra(graph, start_vertex))
