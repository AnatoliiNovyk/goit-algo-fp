import heapq
from typing import Dict, List, Tuple, Any

def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]], start_vertex: Any) -> Dict[Any, float]:
    """
    Реалізація алгоритму Дейкстри для знаходження найкоротших шляхів
    у графі з використанням бінарної купи.

    Важливо: Алгоритм коректно працює тільки для графів 
    з ребрами невід'ємної ваги.

    :param graph: Граф, представлений у вигляді словника суміжності.
    :param start_vertex: Початкова вершина.
    :return: Словник з найкоротшими відстанями.
    """
    # --- Валідація вхідних даних ---
    if start_vertex not in graph:
        # Можна повернути порожній словник або викликати виняток
        raise KeyError(f"Стартова вершина '{start_vertex}' відсутня у графі.")

    distances: Dict[Any, float] = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    
    priority_queue: List[Tuple[float, Any]] = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# --- Демонстрація ---

graph_example = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
try:
    shortest_paths = dijkstra(graph_example, start_node)
    print(f"Найкоротші шляхи від вершини '{start_node}':")
    for vertex, distance in shortest_paths.items():
        print(f"До вершини {vertex}: {distance}")
except KeyError as e:
    print(e)
