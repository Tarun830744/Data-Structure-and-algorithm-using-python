class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("\nlinked list is empty")
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data,end ="-->")
                temp = temp.next
            print(temp.data, "--->",self.head.data)

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self,x):
        if self.head is None:
            print( 'List is Empty!!! searching is not possible')
        else:
            temp = self.head
            while temp.next != self.head:
                if temp.data == x:
                    print("Node is present")
                temp = temp.next
            else:
                print("node is not present")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head

    def begin_delete(self):
        if self.head is None:
            print("\n linked list is empty")
        else:
            temp1 = self.head
            temp2 = self.head
            if temp1.next == None:
                self.head = None
            else:
                while temp1.next != self.head:
                    temp1 = temp1.next
                self.head = temp2.next
                temp1.next = self.head

    def end_delete(self):
        if self.head is None:
            print("\n linked list is empty")
        else:
            temp1 = self.head
            if temp1.next == None:
                self.head = None
            else:
                while temp1.next != self.head:
                    temp2 = temp1
                    temp1 = temp1.next
                temp2.next = self.head

list1 = linkedlist()
list1.add_begin(50)
list1.add_begin(60)
list1.add_begin(70)
list1.printList()










