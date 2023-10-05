class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def get_tail(self):
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current

    def deleteMiddle(self):
        if not self.head:
            return
        
        head_node = self.head
        tail_node = self.get_tail()

        prev_head = None
        prev_tail = None

        while head_node and tail_node and head_node != tail_node and head_node.next != tail_node:
            prev_head = head_node
            head_node = head_node.next

            prev_tail = tail_node
            tail_node = self.head
            while tail_node.next != prev_tail:
                tail_node = tail_node.next

        if head_node == tail_node:
            if prev_head:
                prev_head.next = head_node.next
        else: 
            if prev_head:
                prev_head.next = tail_node

# Test
list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

list.deleteMiddle()

current = list.head
while current:
    print(current.data)
    current = current.next
