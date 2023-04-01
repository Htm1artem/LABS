class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLMap:
    def __init__(self, root=None):
        self.root = root

    def __del__(self):
        self.root = None

    def add(self, key, value):
        self.root = self._add(self.root, key, value)

    def _add(self, root, key, value):
        if not root:
            return AVLNode(key, value)
        elif key < root.key:
            root.left = self._add(root.left, key, value)
        elif key == root.key:
            root.value = value
        else:
            root.right = self._add(root.right, key, value)

        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._height(z.left),
                           self._height(z.right))
        y.height = 1 + max(self._height(y.left),
                           self._height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._height(z.left),
                           self._height(z.right))
        y.height = 1 + max(self._height(y.left),
                           self._height(y.right))

        return y

    def _height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._height(root.left) - self._height(root.right)

    def get(self, key):
        if self.root is not None:
            return self._get(self.root, key)
        return None

    def _get(self, node, key):
        if node is None:
            return None
        elif node.key == key:
            return node.value
        elif key < node.key:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)

    def update(self, key, new_value):
        self.root = self._update(self.root, key, new_value)

    def _update(self, node, key, new_value):
        if not node:
            return None

        if node.key == key:
            node.value = new_value
        elif key < node.key:
            node.left = self._update(node.left, key, new_value)
        else:
            node.right = self._update(node.right, key, new_value)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node
    
    def delete_all(self):
        self.root = None

    def is_empty(self):
        return self.root is None