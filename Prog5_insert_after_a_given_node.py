# insert after a given node
# not the position but the node itself is specified
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, node_name, new_node_value):
        # new node initialize
        new_node = Node(new_node_value)

        # temp storing previous node pointer
        temp = node_name.next
        # assigning previous node pointer to our new node
        node_name.next = new_node
        # new node pointer now points to the previously
        # stored temp pointer
        new_node.next = temp

    def printlist(self):
        # temp = self.head
        # while temp:
        #     print(temp.data, '-->', end=' ')
        #     temp = temp.next
        # print()
        # always use temp = self.head because it will
        # permanently change the head to end of llist
        # otherwise, so even if we print 2 times it will
        # only show one time
        while self.head:
            # temp = self.head
            print(self.head.data, '-->', end=' ')
            self.head = self.head.next
        print()


llist = LinkedList()
llist.head = Node(3)
second = Node(5)
third = Node(7)

llist.head.next = second
second.next = third

llist.printlist()

llist.insert_after(second, 13)
llist.printlist()
