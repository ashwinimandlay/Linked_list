# reverse linked list permanently
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


def reverse(llist):
    # Write your code here
    if llist is None or llist.next is None:
        return llist
    else:
        # remaining is always the head_node (8 in this case)
        remaining = reverse(llist.next)
        llist.next.next = llist
        llist.next = None
        return remaining
    # at the very end recursion we returned remaining


lis = [2, 3, 4, 6, 8]
llist = LinkedList()
for _ in lis:
    llist.insert_in_llist(_)
llist.printlist()

# at end remaining is head node, but we haven't assigned it yet
# right now llist head is still previous one (i.e 2)
# so here we assign head_node = remaining (i.e 8)
llist.head = reverse(llist.head)
llist.printlist()
