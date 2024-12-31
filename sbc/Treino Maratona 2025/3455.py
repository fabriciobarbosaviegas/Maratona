def maximize_questions(A, B, C, target):
    graph_to_dyn = 3 / 2
    graph_to_geom = 5 / 2 
    
    if target == 'A': 
        total_graphs = A + (B * graph_to_dyn) + (C * (graph_to_geom / 1))
        return int(total_graphs)
    elif target == 'B':
        total_dyn = B + (A / graph_to_dyn) + (C * (graph_to_geom / graph_to_dyn))
        return int(total_dyn)
    elif target == 'C':
        total_geom = C + (A / (graph_to_geom / 1)) + (B * (graph_to_dyn / graph_to_geom))
        return int(total_geom)


A, B, C = map(int, input().split())
target = input().strip()

print(maximize_questions(A, B, C, target))