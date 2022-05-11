# inserting node at end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, num):
        # initialize end node
        new_end_node = Node(num)
        temp = self.head
        # if sel.head is not empty(None) then
        # assign num as head
        if not self.head:
            temp.data = num
        # else iterate until end node then add new node at end
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_end_node

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
llist.insert_at_end(10)
llist.printlist()

