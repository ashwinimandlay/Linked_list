# print linked list in reverse (using recursion)
# RECURSION very likely used in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_llist(self, node_value):
        node = Node(node_value)
        temp = self.head
        if temp is None:
            self.head = node
        else:
            while temp.next:
                temp = temp.next
            temp.next = node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, '-->', end=' ')
            temp = temp.next
        print()


def print_reverse_of_llist(llist_head):
    temp = llist_head
    if temp:
        # this is --> reverse(reverse(reverse(reverse())))
        # first the last one completes and print 8-->6-->4...
        print_reverse_of_llist(temp.next)
        print(temp.data, end=' --> ')


lis = [2, 3, 4, 6, 8]
llist = LinkedList()
for _ in lis:
    llist.insert_in_llist(_)
llist.printlist()

# printing reversed of linked list
print_reverse_of_llist(llist.head)
