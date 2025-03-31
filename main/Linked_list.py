class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def __str__(self):
        current_node = self.head
        result = ""
        while current_node:
            result = result + str(current_node.data)+"---> "
            current_node = current_node.next
        result = result[0:-5:1]
        return result
    def insert_at_end(self, data):
        new_node = ListNode(data)
        current_node = self.head
        if self.head is None:
            self.head = new_node
            return
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            return
    def delete_first(self):
        if self.head is None:
            return None
        else:
            current_node = self.head
            current_node_1 = current_node.next
            self.head = current_node_1
            return current_node.data
    def delete_last(self):
        if self.head is None:
            return None
        else:
            current_node = self.head
            current_node_1 = current_node
            while current_node.nextnext is not None:
                current_node_1 = current_node
                current_node = current_node.next
            current_node_1.next = None
            return current_node.data
    def insert_by_index(self, data, ind):
        new_node = ListNode(data)
        current_node = self.head
        while current_node.next != ind:
            current_node = current_node.next
        current_node.next = new_node
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




ll = LinkedList()
ll.insert_at_begin(1)
ll.insert_at_begin(2)
ll.insert_at_begin(3)
ll.insert_at_begin(4)
ll.insert_at_begin(5)
ll.insert_at_begin(6)
print(ll.find_middle())

print(ll)