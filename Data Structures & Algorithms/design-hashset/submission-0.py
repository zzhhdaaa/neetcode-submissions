class Node:

    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.array = [None for _ in range(10000)]

    def add(self, key: int) -> None:
        mod = key%10000
        if self.array[mod] is None:
            self.array[mod] = Node(key)
        else:
            prev = None
            curr = self.array[mod]
            while curr:
                if curr.key == key:
                    return
                prev = curr
                curr = curr.next
            prev.next = Node(key)

    def remove(self, key: int) -> None:
        mod = key%10000
        if self.array[mod] is None:
            return
        else:
            prev = None
            curr = self.array[mod]

            while curr and curr.key != key:
                prev = curr
                curr = curr.next
            
            if curr is None:
                return
            elif curr is not None and prev is None:
                self.array[mod] = curr.next
            else:
                prev.next = curr.next

    def contains(self, key: int) -> bool:
        mod = key%10000
        if self.array[mod] is None:
            return False
        else:
            curr = self.array[mod]
            while curr:
                if curr.key == key:
                    return True
                curr = curr.next
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)