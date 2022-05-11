# inserting node at beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, num):
        # declare new node
        new_start_node = Node(num)
        # previous llist.head is now what new node will point
        new_start_node.next = self.head
        # llist.head is now pointing to new node
        self.head = new_start_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, '-->', end=' ')
            temp = temp.next
        print()


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printlist()
llist.add_at_beginning(7)
llist.printlist()

