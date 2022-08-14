class Node:
    def __init__(self, value, parent):
        self.parent = parent
        if isinstance(value, int):
            self.value = value
            self.left = None
            self.right = None
        elif isinstance(value, list):
            self.value = None
            self.left = Node(value[0], self)
            self.right = Node(value[1], self)
        else:
            self.value = None
            self.left = None
            self.right = None

    def __add__(self, other):
        node = Node(None, None)
        node.left = self.copy()
        node.right = other.copy()
        node.left.parent = node
        node.right.parent = node
        node.reduce()
        return node

    def copy(self):
        node = Node(None, None)
        node.value = self.value
        if self.has_left():
            node.left = self.left.copy()
            node.left.parent = node
        if self.has_right():
            node.right = self.right.copy()
            node.right.parent = node
        return node

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def is_leaf(self):
        return self.value is not None

    def is_pair(self):
        return not self.is_leaf()

    def is_simple_pair(self):
        return self.is_pair() and self.left.is_leaf() and self.right.is_leaf()

    def has_parent(self):
        return self.parent is not None

    def predecessor(self):
        if not self.has_parent():
            return None
        if self == self.parent.left:
            return self.parent.predecessor()
        predecessor = self.parent.left
        while predecessor.has_right():
            predecessor = predecessor.right
        return predecessor

    def successor(self):
        if not self.has_parent():
            return None
        if self == self.parent.right:
            return self.parent.successor()
        predecessor = self.parent.right
        while predecessor.has_left():
            predecessor = predecessor.left
        return predecessor

    def explode(self):
        left_value = self.left.value
        right_value = self.right.value
        left_node = self.predecessor()
        if left_node is not None:
            left_node.value += left_value
        right_node = self.successor()
        if right_node is not None:
            right_node.value += right_value
        self.value = 0
        self.left = None
        self.right = None

    def split(self):
        left_value = self.value // 2
        right_value = self.value - left_value
        self.value = None
        self.left = Node(left_value, self)
        self.right = Node(right_value, self)

    def reduce(self):

        changed = [False]

        def check_explosion(node, depth):
            if node is None or changed[0]:
                return
            if depth >= 4 and node.has_left() and node.has_right():
                node.explode()
                changed[0] = True
                return
            check_explosion(node.left, depth + 1)
            check_explosion(node.right, depth + 1)

        def check_split(node):
            if node is None or changed[0]:
                return
            if node.is_leaf() and node.value >= 10:
                node.split()
                changed[0] = True
                return
            check_split(node.left)
            check_split(node.right)

        check_explosion(self, 0)
        if changed[0]:
            self.reduce()
            return
        check_split(self)
        if changed[0]:
            self.reduce()

    def magnitude(self):
        if self.is_leaf():
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()
