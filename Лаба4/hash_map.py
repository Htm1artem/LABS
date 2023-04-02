class Node:
    def __init__(self, key, value):
        self.key = key
        self.next_node = None
        self.value = value


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 50
        self.bucket = [None] * self.capacity

    def hash(self, key):
        hash_sum = 0
        for idx, c in enumerate(key):
            hash_sum += (idx + len(key)) ** ord(c)
        return hash_sum % self.capacity

    def add(self, key, value):
        index = self.hash(key)
        node = self.bucket[index]

        if node is None:
            self.bucket[index] = Node(key, value)
            self.size += 1
            return

        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next_node

        prev.next_node = Node(key, value)
        self.size += 1

    def get(self, key):
        index = self.hash(key)
        node = self.bucket[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next_node

        return None

    def delete(self, key):
        index = self.hash(key)
        node = self.bucket[index]
        prev = None

        while node is not None:
            if node.key == key:
                self.size -= 1
                result = node.value
                if prev is None:
                    self.bucket[index] = node.next_node
                else:
                    prev.next_node = node.next_node
                return result
            prev = node
            node = node.next_node

        return None

    def clear(self):
        self.bucket = [None] * self.capacity
        self.size = 0


    def items(self):
        items_list = []
        for node in self.bucket:
            while node is not None:
                items_list.append((node.key, node.value))
                node = node.next_node
        return items_list

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key) is not None
