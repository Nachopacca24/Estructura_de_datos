class Node:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return '({})'.format(self.data)

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def traverse(self, subtree: Node):
        print(subtree)
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)
        if subtree.right_child is not None:
            self.traverse(subtree.right_child)

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, subtree: Node):
        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)
        else:
            print('Value already exists in tree...')

    def search(self, key: int) -> bool:
        if self.root is None:
            return False
        else:
            return self._search(key, self.root)

    def _search(self, key: int, subtree: Node) -> bool:
        if key == subtree.data:
            return True
        elif key < subtree.data and subtree.left_child is not None:
            return self._search(key, subtree.left_child)
        elif key > subtree.data and subtree.right_child is not None:
            return self._search(key, subtree.right_child)
        else:
            return False

    def find_min(self, subtree: Node) -> Node:
        while subtree.left_child is not None:
            subtree = subtree.left_child
        return subtree

    def find_max(self, subtree: Node) -> Node:
        while subtree.right_child is not None:
            subtree = subtree.right_child
        return subtree

    def print_pretty(self):
        if self.root is not None:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")

    def _build_tree_string(self, node: Node):
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def delete(self, value: int):
        self.root = self._delete(self.root, value)

    def _delete(self, subtree: Node, value: int):
        if subtree is None:
            return subtree

        # Buscar el nodo a eliminar
        if value < subtree.data:
            subtree.left_child = self._delete(subtree.left_child, value)
        elif value > subtree.data:
            subtree.right_child = self._delete(subtree.right_child, value)
        else:
            # Caso 1: Nodo sin hijos
            if subtree.left_child is None and subtree.right_child is None:
                return None

            # Caso 2: Nodo con un solo hijo
            if subtree.left_child is None:
                return subtree.right_child
            elif subtree.right_child is None:
                return subtree.left_child

            # Caso 3: Nodo con dos hijos (usar el sucesor inorden)
            min_larger_node = self.find_min(subtree.right_child)
            subtree.data = min_larger_node.data
            subtree.right_child = self._delete(subtree.right_child, min_larger_node.data)

        return subtree
