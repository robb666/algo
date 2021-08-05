
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)  # !!!


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def rem0ve_at(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_lenght():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new = Node(data, itr.next)
                itr.next = new
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, have_data, nev_data):
        itr = self.head
        while itr:
            if itr.data == have_data:
                new = Node(nev_data, itr.next)
                itr.next = new
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        itr = self.head
        if itr.data == data:
            itr = self.head.next

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next

    def print(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def print_forward(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ', '
            itr = itr.next
        print(llstr)


    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()


