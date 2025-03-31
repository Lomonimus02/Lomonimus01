def find_middle(self):
    if self.head is None:
        return None
    current_node = self.head
    count = 0
    while current_node.next is not None:
        current_node = current_node.next
        count += 1
    if count % 2 == 1:
        count = count // 2 + 1
        current_node = self.head
    elif count == 1:
        count = count
        current_node = self.head
    else:
        count = count // 2
        current_node = self.head
    while count != 0:
        current_node = current_node.next
        count += -1
    return current_node.data