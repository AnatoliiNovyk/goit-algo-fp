import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
from typing import List, Optional, Dict, Any, Tuple

# --- Базовий код, наданий в інструкції, з покращеннями ---

class Node:
    """Клас для представлення вузла бінарного дерева."""
    def __init__(self, key, color="skyblue"):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph: nx.DiGraph, node: Optional[Node], pos: Dict[str, Tuple[float, float]], x: float = 0, y: float = 0, layer: int = 1) -> None:
    """
    Рекурсивно додає ребра та вузли дерева до графа networkx.
    Функція не повертає значення, оскільки модифікує об'єкти graph та pos "на місці".
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            # Розрахунок горизонтальної позиції для рознесення вузлів на глибині
            l_x = x - 1 / 2 ** layer
            pos[node.left.id] = (l_x, y - 1)
            add_edges(graph, node.left, pos, x=l_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            # Розрахунок горизонтальної позиції
            r_x = x + 1 / 2 ** layer
            pos[node.right.id] = (r_x, y - 1)
            add_edges(graph, node.right, pos, x=r_x, y=y - 1, layer=layer + 1)

def draw_tree(tree_root: Node) -> None:
    """Візуалізує бінарне дерево."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# --- Рішення Завдання 4 ---

def build_heap_tree(heap_array: List[Any], i: int = 0) -> Optional[Node]:
    """
    Рекурсивно будує бінарне дерево з масиву, що представляє купу.
    """
    if i < len(heap_array):
        node = Node(heap_array[i])
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        node.left = build_heap_tree(heap_array, left_index)
        node.right = build_heap_tree(heap_array, right_index)
        return node
    return None

# --- Демонстрація ---

# Створимо масив і перетворимо його на бінарну купу (мін-купу)
raw_array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapq.heapify(raw_array)

# Будуємо дерево з купи
heap_tree_root = build_heap_tree(raw_array)

# Візуалізуємо дерево
if heap_tree_root:
    print("Візуалізація бінарної купи:")
    draw_tree(heap_tree_root)
else:
    print("Купа порожня, нічого візуалізувати.")
