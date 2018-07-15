class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_prev):
        self.prev_node = new_prev

class linkedList:
    def __init__(self):
        self._head = None
        self._length = 0

    def add(self, data):
        n = Node(data)
        if self._head:
            self._head._previous = n

        self._head = n
        self._length += 1

    def search(self,cargo):
        node = self._head
        while (node and node._cargo != cargo):
            node = node._next
        return node

    def delete(self,cargo):
        node = self.search(cargo)
        if node:
            prev = node._previous
            nx = node._next
            if prev:
                prev._next = node._next
            else:
                self._head = nx
                nx._previous = None
            if nx:
                nx._previous = prev
            else:
                prev._next = None
        self._length -= 1

    def __str__(self):
        print 'Size of linked list: ',self._length
        node = self._head
        while node:
            print node
            node = node._next
