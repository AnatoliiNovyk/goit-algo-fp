from typing import Any, Optional

class Node:
    """Клас для представлення вузла однозв'язного списку."""
    def __init__(self, data: Any = None):
        self.data: Any = data
        self.next: Optional[Node] = None

class LinkedList:
    """Клас для представлення однозв'язного списку."""
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_end(self, data: Any) -> None:
        """Додає вузол в кінець списку."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self) -> None:
        """Виводить вміст списку."""
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        nodes.append("None")
        print(" -> ".join(nodes))

    # --- Завдання 1.1: Реверсування ---
    def reverse(self) -> None:
        """
        Реверсує однозв'язний список, змінюючи посилання між вузлами.
        """
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    # --- Завдання 1.2: Сортування злиттям ---
    def sort(self) -> None:
        """
        Сортує список, використовуючи алгоритм сортування злиттям.
        """
        self.head = self._merge_sort(self.head)

    @staticmethod
    def _split_list(head: Optional[Node]) -> tuple[Optional[Node], Optional[Node]]:
        """Розділяє список на дві половини."""
        # Умова `if not head or not head.next` тут зайва,
        # оскільки цикл `while` коректно обробляє ці випадки.
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if slow:
            mid = slow.next
            slow.next = None
            return head, mid
        return head, None


    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        """Рекурсивна функція для сортування злиттям."""
        if not head or not head.next:
            return head
        
        left_half, right_half = self._split_list(head)
        
        left = self._merge_sort(left_half)
        right = self._merge_sort(right_half)
        
        # Використання ітеративного злиття для уникнення помилок рекурсії
        return self._iterative_merge(left, right)

    # --- Завдання 1.3: Об'єднання відсортованих списків ---
    @staticmethod
    def _iterative_merge(left: Optional[Node], right: Optional[Node]) -> Optional[Node]:
        """
        Ітеративно об'єднує два відсортовані списки.
        Цей підхід є більш надійним для дуже довгих списків,
        оскільки він не залежить від глибини рекурсії Python.
        """
        dummy = Node()
        current = dummy

        while left and right:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        current.next = left or right
        return dummy.next
    
    @staticmethod
    def merge_two_sorted_lists(l1: 'LinkedList', l2: 'LinkedList') -> 'LinkedList':
        """
        Об'єднує два зовнішні відсортовані екземпляри LinkedList.
        """
        merged_list = LinkedList()
        merged_list.head = LinkedList._iterative_merge(l1.head, l2.head)
        return merged_list

# --- Демонстрація ---
print("--- 1. Реверсування ---")
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
print("Початковий список:")
ll.print_list()
ll.reverse()
print("Реверсований список:")
ll.print_list()
print("\n" + "-"*30 + "\n")

print("--- 2. Сортування ---")
ll_sort = LinkedList()
ll_sort.insert_at_end(5)
ll_sort.insert_at_end(1)
ll_sort.insert_at_end(9)
ll_sort.insert_at_end(3)
print("Несортований список:")
ll_sort.print_list()
ll_sort.sort()
print("Відсортований список:")
ll_sort.print_list()
print("\n" + "-"*30 + "\n")

print("--- 3. Об'єднання двох відсортованих списків ---")
ll1 = LinkedList()
ll1.insert_at_end(1)
ll1.insert_at_end(3)
ll1.insert_at_end(5)
ll2 = LinkedList()
ll2.insert_at_end(2)
ll2.insert_at_end(4)
ll2.insert_at_end(6)
print("Перший список:")
ll1.print_list()
print("Другий список:")
ll2.print_list()
merged_ll = LinkedList.merge_two_sorted_lists(ll1, ll2)
print("Об'єднаний відсортований список:")
merged_ll.print_list()
