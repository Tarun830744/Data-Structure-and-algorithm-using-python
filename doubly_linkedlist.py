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
            while temp is not None:
                print(temp.data,end ="<-->")
                temp= temp.next

    def add_begin(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.previous = newnode
            self.head = newnode

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous =temp

    def between_list(self,data,position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp is not None:
                if position == temp.data:
                    break
                temp = temp.next
            else:
                print("Given node is not found in the list!!! Insertion not possible!!!")
            try:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.previous = temp
                if temp.next is not None:
                    temp.next.previous = new_node
                temp.next = new_node
            except:
                pass

    def begin_delete(self):
        if self.head is None:
            print("\n linked list is empty")
        else:
            temp = self.head
            if temp.next == None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.previous = None

    def delete_by_value(self ,x):
        if self.head is None:
            print( 'List is Empty!!! Deletion is not possible')
        elif self.head.next == None:
            if x == self.head.data:
                self.head = None
            else:
                pass
        else:
            temp = self.head
            while temp is not None:
                if x == temp.data:
                    break
                temp = temp.next
            else:
                print("Given node is not found in the list!!! Insertion not possible!!!")
            if temp == self.head:
                self.head = self.head.next
                self.head.previous = None
            elif temp.next == None:
                temp.previous.next = None
            else:
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
list1 = linkedlist()
list1.add_end(50)
list1.add_end(60)
list1.add_end(70)
list1.printList()



