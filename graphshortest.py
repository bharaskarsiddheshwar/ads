class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, from_vertex, to_vertex, weight):
        self.adj_matrix[from_vertex][to_vertex] = weight
        self.adj_matrix[to_vertex][from_vertex] = weight  # Assuming an undirected graph
    
    def find_shortest_path(self, start_vertex, end_vertex):
        visited = [False] * self.vertices
        distance = [float('inf')] * self.vertices
        distance[start_vertex] = 0
        
        for _ in range(self.vertices - 1):
            min_distance = float('inf')
            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_distance:
                    min_distance = distance[v]
                    current_vertex = v
            
            visited[current_vertex] = True
            
            for v in range(self.vertices):
                if (
                    not visited[v] and 
                    self.adj_matrix[current_vertex][v] > 0 and 
                    distance[current_vertex] + self.adj_matrix[current_vertex][v] < distance[v]
                ):
                    distance[v] = distance[current_vertex] + self.adj_matrix[current_vertex][v]
        
        return distance[end_vertex]

if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)

    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        from_vertex, to_vertex, weight = map(int, input("Enter edge (from to weight): ").split())
        g.add_edge(from_vertex, to_vertex, weight)

    start_vertex = int(input("Enter the starting vertex: "))
    end_vertex = int(input("Enter the ending vertex: "))

    shortest_distance = g.find_shortest_path(start_vertex, end_vertex)

    print(f"Shortest distance from vertex {start_vertex} to vertex {end_vertex} is {shortest_distance}")
