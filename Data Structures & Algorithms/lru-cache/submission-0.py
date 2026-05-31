class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    # each time a key(node) is used(get/put), it get moved/added to the place after tail
    # only when added to the list, we need to potentially remove one from the bottom of the list

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = dict()

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail # dummy head on the most recent side
        self.tail.prev = self.head # dummy tail on the least recent side
        
    def move_to_head(self, node: Node):
        # move an existing node to the head
        # _ 0 _
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    def add_to_head(self, node: Node):
        # add a new node to the head, potentially remove one from the tail
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

        self.node_map[node.key] = node
        if len(self.node_map) <= self.capacity:
            return
        
        LAST = self.tail.prev
        LAST.prev.next = LAST.next
        LAST.next.prev = LAST.prev
        self.node_map.pop(LAST.key)

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        # move the node to the head, then return
        self.move_to_head(self.node_map[key])
        return self.node_map[key].val

    def put(self, key: int, value: int) -> None:
        # key in map: update and move the node to the head
        if key in self.node_map:
            self.node_map[key].val = value
            self.move_to_head(self.node_map[key])

        # key not in map: put the node to the head, and potentially remove from tail
        else:
            node = Node(key, value)
            self.add_to_head(node)
        
