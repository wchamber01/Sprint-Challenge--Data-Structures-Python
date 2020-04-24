from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if capacity not full
        if len(self.storage) < self.capacity:
            # add item to tail i.e. most recently added
            self.storage.add_to_tail(item)
            # set pointer to tail
            self.current = self.storage.tail
        # if capacity is full
        if len(self.storage) == self.capacity:
            # add item to tail
            self.current.value = item
            if self.current is self.storage.tail:
                # move pointer to head
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # add values from storage to list_buffer_contents
        list_item = self.storage.head
        while list_item:
            if list_item.value == None:
                list_item = list_item.next
            else:
                list_buffer_contents.append(list_item.value)
                list_item = list_item.next
        return list_buffer_contents

    # ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
