from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if capacity not full
        if len(self.storage) < self.capacity:
            # add item to tail
            self.storage.add_to_tail(item)
        # if capacity is full
        if len(self.storage) == self.capacity:
            # del head
            self.storage.delete(self.head)
            # del self.head
            # add item to tail
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

    # TODO: Your code here
    # if self.list_buffer_contents:
    # return list_buffer_contents

    # ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
