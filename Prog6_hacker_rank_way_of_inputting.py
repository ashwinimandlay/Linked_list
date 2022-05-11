# alternate way of inputting values in
# linked list (Hacker Rank ques)
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_nodes(self, node_value):
        node = Node(node_value)

        # instead of using temp we are using self.tail becoz
        # we are adding to the right

        # if we use temp then we will be adding to the left

        # if not self.head condition is true when self.head
        # is empty (or no node in linked list)
        if not self.head:
            self.head = node
        else:
            # previous element pointer points to the
            # next element
            self.tail.next = node

        # self.tail always points at last element
        self.tail = node


# print function can be written outside of class too
def print_linked_list(linked_list_head):
    # we can also pass linked list
    # then linked_list_head is replaced by llst.head
    temp = linked_list_head
    while temp:
        print(temp.data, '-->', end=' ')
        temp = temp.next


# elements of linked list
lis = [3, 4, 8]
llist = LinkedList()
for i in lis:
    llist.insert_nodes(i)

print_linked_list(llist.head)
