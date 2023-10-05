class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def reverse(list1, list2):
    carry = 0
    dummy = Node()
    current = dummy

    while list1 or list2 or carry:
        sum_val = carry
        if list1:
            sum_val += list1.data
            list1 = list1.next
        if list2:
            sum_val += list2.data
            list2 = list2.next
        carry, val = divmod(sum_val, 10)
        current.next = Node(val)
        current = current.next

    return dummy.next

def forward(list1, list2):
    if list_len(list1) < list_len(list2):
        list1, list2 = list2, list1

    carry, head = add_nodes(list1, list2, list_len(list1) - list_len(list2))
    if carry:
        new_node = Node(carry)
        new_node.next = head
        head = new_node
    return head

def list_len(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count

def add_nodes(list1, list2, offset):
    if not list1:
        return 0, None
    if offset:
        carry, next_node = add_nodes(list1.next, list2, offset - 1)
    else:
        carry, next_node = add_nodes(list1.next, list2.next, 0)
    sum_val = list1.data + (list2.data if offset == 0 else 0) + carry
    new_carry, val = divmod(sum_val, 10)
    current = Node(val)
    current.next = next_node
    return new_carry, current

# Test
list1 = Node(7)
list1.next = Node(1)
list1.next.next = Node(6)
list2 = Node(5)
list2.next = Node(9)
list2.next.next = Node(2)

result = reverse(list1, list2)
while result:
    print(result.data, end=" -> ")
    result = result.next
print()

list1 = Node(6)
list1.next = Node(1)
list1.next.next = Node(7)
list2 = Node(2)
list2.next = Node(9)
list2.next.next = Node(5)

result = forward(list1, list2)
while result:
    print(result.data, end=" -> ")
    result = result.next
