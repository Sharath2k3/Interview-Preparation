def graph_coloring(graph):
    """
    Greedy algorithm for graph coloring.
    
    Args:
    - graph: Dictionary where keys are nodes and values are lists of neighbors.

    Returns:
    - colors: Dictionary with nodes as keys and their assigned colors as values.
    """
    # Initialize a dictionary to store the color of each vertex
    colors = {}
    
    # Iterate over each vertex in the graph
    for vertex in graph:
        # Find the colors of all adjacent vertices
        neighbor_colors = {colors[neighbor] for neighbor in graph[vertex] if neighbor in colors}
        
        # Assign the smallest available color
        color = 1
        while color in neighbor_colors:
            color += 1
        colors[vertex] = color

    return colors


# Example Usage
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    colors = graph_coloring(graph)
    print("Vertex Colors:")
    for vertex, color in colors.items():
        print(f"Vertex {vertex}: Color {color}")
