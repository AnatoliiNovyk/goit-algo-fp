import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Клас Node та функції візуалізації залишаються без змін
class Node:
    """Клас для представлення вузла бінарного дерева."""
    def __init__(self, key, color="#1296F0"):
        self.left: 'Node' | None = None
        self.right: 'Node' | None = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root, title=""):
    """Візуалізує бінарне дерево з певним заголовком."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# --- Нова допоміжна функція для скидання кольорів ---
def reset_colors(node: Node | None, default_color="#1296F0"):
    """Рекурсивно скидає колір вузлів до початкового."""
    if node:
        node.color = default_color
        reset_colors(node.left, default_color)
        reset_colors(node.right, default_color)

# Функції обходу DFS та BFS залишаються без змін
def dfs(root: Node):
    if not root: return []
    visited_nodes, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            visited_nodes.append(node)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
    return visited_nodes

def bfs(root: Node):
    if not root: return []
    visited_nodes, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited_nodes.append(node)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return visited_nodes

def generate_colors(n):
    colors = []
    for i in range(n):
        shade = 255 - int(200 * (i / (n - 1))) if n > 1 else 128
        colors.append(f'#0000{shade:02x}')
    return colors

# --- Демонстрація ---

# Створення дерева (тільки один раз)
root = Node(0)
root.left = Node(4)
root.right = Node(1)
root.left.left = Node(5)
root.left.right = Node(10)
root.right.left = Node(3)
root.right.right = Node(2)

# 1. Візуалізація обходу в глибину (DFS)
dfs_nodes = dfs(root)
colors = generate_colors(len(dfs_nodes))
for i, node in enumerate(dfs_nodes):
    node.color = colors[i]
draw_tree(root, "Обхід в глибину (DFS)")

# 2. Візуалізація обходу в ширину (BFS)
# Скидаємо кольори існуючого дерева замість його перестворення
reset_colors(root) 

bfs_nodes = bfs(root)
colors = generate_colors(len(bfs_nodes))
for i, node in enumerate(bfs_nodes):
    node.color = colors[i]
draw_tree(root, "Обхід в ширину (BFS)")
