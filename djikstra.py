import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra_with_visualization(graph, source, target):
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0
    predecessor = {node: None for node in graph.nodes}
    visited = set()

    # Priority queue for nodes
    priority_queue = [(0, source)]  # (distance, node)

    # Precompute layout for consistent visualization
    pos = nx.spring_layout(graph)

    step = 1
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the node is already visited
        if current_node in visited:
            continue
        visited.add(current_node)

        # Visualize the current state of the graph
        print(f"Step {step}: Visiting Node = {current_node}, Distance = {current_distance}")
        visualize_graph(graph, source, target, visited, distances, predecessor, pos)
        step += 1

        # Update distances to neighbors
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Backtrack to find the shortest path
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessor[current]

    # Final visualization with shortest path
    visualize_graph(graph, source, target, visited, distances, predecessor, pos, final_path=path)

    return path, distances[target]


def visualize_graph(graph, source, target, visited, distances, predecessor, pos, final_path=None):
    # Node colors
    node_colors = []
    for node in graph.nodes:
        if node == source:
            node_colors.append('red')  # Start node
        elif node == target:
            node_colors.append('green')  # Goal node
        elif node in visited:
            node_colors.append('skyblue')  # Visited nodes
        else:
            node_colors.append('yellow')  # Unvisited nodes

    # Edge colors
    edge_colors = ['black'] * len(graph.edges)

    if final_path:
        # Highlight the final path
        path_edges = list(zip(final_path, final_path[1:]))
        for i, edge in enumerate(graph.edges):
            if edge in path_edges or (edge[1], edge[0]) in path_edges:
                edge_colors[i] = 'green'

    # Draw graph
    plt.figure(figsize=(10, 8))
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=800,
        font_size=12,
        font_color="black",
    )

    # Show edge weights
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Network Graph Visualization")
    plt.show()


def main():
    print("Enter the graph details:")
    print("Example: Enter edges in format `A B 4` (where A and B are nodes, 4 is weight). Type 'done' to finish.")

    G = nx.Graph()

    while True:
        edge_input = input("Enter edge (or 'done' to finish): ").strip()
        if edge_input.lower() == 'done':
            break
        try:
            node1, node2, weight = edge_input.split()
            weight = int(weight)
            G.add_edge(node1, node2, weight=weight)
        except ValueError:
            print("Invalid format! Enter in the format `A B 4`.")

    source = input("Enter the source node: ").strip()
    target = input("Enter the target node: ").strip()

    if source not in G.nodes or target not in G.nodes:
        print("Invalid source or target node!")
        return

    shortest_path, total_cost = dijkstra_with_visualization(G, source, target)
    print(f"\nShortest Path: {' -> '.join(shortest_path)}")
    print(f"Total Cost: {total_cost}")


if __name__ == "__main__":
    main()
