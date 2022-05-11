# traversing through list
# nodes are fixed
# head is traversing
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # nodes are fixed so don't use this
    # def printlist(self):
    #     while self is not None:
    #         print(self.data)
    #         self = self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
# becoz of this statement we come out of loop
# third.next = None

llist.printlist()
