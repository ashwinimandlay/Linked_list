# linked list intro
# NOTE: python have names (and not variables) they just point
#       to the element or object
# Node class is used for data and next pointer
# linked list class just initializes the head once
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


llist = LinkedList()
# llist is a LinkedList object

llist.head = Node(1)
# llist.head is a Node object
# similarly second and third
second = Node(2)
third = Node(3)

# these points to the next object
llist.head.next = second
second.next = third

