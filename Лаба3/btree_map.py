from collections import deque

class TreeNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinaryTreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
            return
        q = [self.root]
        while q:
            curr = q.pop(0)
            if not curr.left:
                curr.left = TreeNode(key, value)
                break
            else:
                q.append(curr.left)
            if not curr.right:
                curr.right = TreeNode(key, value)
                break
            else:
                q.append(curr.right)

    def delete_deepest_node(self, deepest_node):
        dq = deque()
        dq.append(self.root)
        parent = None
        while dq:
            curr = dq.popleft()
            if curr is deepest_node:
                if parent is None:  # deepest_node is the root
                    self.root = None
                    return
                if parent.left is deepest_node:
                    parent.left = None
                else:
                    parent.right = None
                return
            if curr.right:
                parent = curr
                dq.append(curr.right)
            if curr.left:
                parent = curr
                dq.append(curr.left)

    def clear(self):
        self.root = None

    def inorder_traversal(self, curr_node):
        inorder_list = []
        if curr_node is None:
            return []
        inorder_list = self.inorder_traversal(curr_node.left)
        inorder_list.append(curr_node)
        inorder_list = inorder_list + self.inorder_traversal(curr_node.right)
        return inorder_list

    def postorder_traversal(self, curr_node):
        postorder_list = []
        if curr_node is None:
            return []
        postorder_list = self.postorder_traversal(curr_node.left)
        postorder_list = postorder_list + self.postorder_traversal(curr_node.right)
        postorder_list.append(curr_node)
        return postorder_list

    def preorder_traversal(self, curr_node):
        preorder_list = []
        if curr_node is None:
            return []
        preorder_list.append(curr_node)
        preorder_list = preorder_list + self.preorder_traversal(curr_node.left)
        preorder_list = preorder_list + self.preorder_traversal(curr_node.right)
        return preorder_list

    def search(self, key):
        node_queue = []
        node_queue.append(self.root)
        while len(node_queue) > 0:
            curr_node = node_queue.pop(0)
            if curr_node.key == key:
                return curr_node.value
            if curr_node.left:
                if curr_node.left.key == key:
                    return curr_node.left.value
                else:
                    node_queue.append(curr_node.left)
            if curr_node.right:
                if curr_node.right.key == key:
                    return curr_node.right.value
                else:
                    node_queue.append(curr_node.right)
    
    def is_empty(self):
        return self.root is None