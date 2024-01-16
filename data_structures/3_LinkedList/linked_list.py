"""Linked List"""

class Node:
    """Define Node"""
    def __init__(self, data=None, next=None):
        """
        Initialize Node
        Node has -
            data: data being stored
            next: address of next element in list
        """
        self.data = data # can contain anything
        self.next = next # pointer to next element

class LinkedList:
    """Define Linked List"""
    def __init__(self):
        """"Define head"""
        self.head = None # poitns to head of linked list

    def insert_at_begining(self, data):
        """Insert data at the begining of the Linked List"""
        node = Node(data, self.head)
        self.head = node

    def print(self):
        """Print List"""
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        """Insert data at the end of linked List"""
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """Create a fresh list from an inserted List"""
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """return length of Linked List"""
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, idx: int):
        """Remove element at a given index"""
        if idx < 0 or idx >= self.get_length():
            raise ValueError('Idx range error')
        if idx == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, idx, data):
        """Insert an input value at a given index"""
        if idx < 0 or idx >= self.get_length():
            raise ValueError("idx range error")
        if idx == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1




if __name__ == '__main__':
    try:
        ll = LinkedList()
        ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
        ll.print()
        print("Length of Linked List", ll.get_length())
        ll.remove_at(2)
        ll.print()
        ll.insert_at(0, 'kiwi')
        ll.print()
        ll.insert_at(2, 'apple')
        ll.print()
    except KeyboardInterrupt:
        exit()
