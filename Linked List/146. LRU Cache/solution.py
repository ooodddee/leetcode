class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dummy = Node()
        self.dummy.pre = self.dummy
        self.dummy.next = self.dummy
        self.key_to_value = {}

    def get_node(self, key):
        if key not in self.key_to_value:
            return None
        node = self.key_to_value[key]
        self.remove(node)
        self.push_front(node)
        return node

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def push_front(self, node):
        node.next = self.dummy.next
        node.pre = self.dummy
        node.next.pre = node
        node.pre.next = node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key_to_value[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.key_to_value) > self.cap:
            back_node = self.dummy.pre
            del self.key_to_value[back_node.key]
            self.remove(back_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)