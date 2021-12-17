class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("\nlinked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end =" ")
                n = n.next
               
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    def between_list(self,data,position):
        n = self.head
        if position < 1:
            print("\nLinked list position start from 1")
        elif position==1:
            self.addbegin(data)
        else:
            for i in range(1,position-1):
                if n is not None:
                    n = n.next
            if n is None:
                print("\n position is out of range")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
    
    def delete_by_value(self ,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("\n Value is not present")
        else:
            n.next = n.next.next

    def search(self,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("\nValue is not present")
        else:
            print("\nvalue is present" ,n.data)
    
    def begin_delete(self):
        if self.head is None:
            print("\n linked list is empty")
        else:
            self.head = self.head.next
    
    def end_delete(self):
        if self.head is None:
            print("\nlinked list is empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    
    def count_fun(self):
        n = self.head
        count = 0
        while n is not None:
            n = n.next
            count = count+1
        print("\nNumber of element in linked list is {}".format(count))

fun = ["Insert at begining","Insert at End","Insert at position","Delete at begining","Delete at End","Delet the value","Search","Count"]

# To give number for operation
def operation():
    for i in range(8):
        print("[{}] = {} ".format(i+1,fun[i]))

def linkedlist_opp():
    if opp == 1:
        value = input("\nEnter value to add at starting of linked list: ")
        list1.add_begin(value)
        list1.printList()

    elif opp ==2:
        value = input("\nEnter value to add at the end of the linked list:")
        list1.add_end(value)
        list1.printList()
    
    elif opp ==3:
        position = int(input("\nEnter a position to add value in linked list: "))
        value = input("\nEnter value to add between in linked list: ")
        list1.between_list(value,position)
        list1.printList()

    elif opp == 4:
        list1.begin_delete()
        print("\n After Delete value linked list :")
        list1.printList()

    elif opp == 5:
        list1.end_delete()
        print("\n After Delete value linked list :")
        list1.printList()

    elif opp == 6 :
        value = input("\nEnter a value which you want to delete")
        list1.delete_by_value(value)
        print("\n After Delete value linked list :")
        list1.printList()
    
    elif opp == 7:
        value = input("\nEnter a value which you want to search")
        list1.search(value)

    elif opp == 8:
        list1.count_fun()

list1 = linkedlist()
value ="Y"
while value=="Y":
    operation()
    opp = int(input("\n To Perform operation enter numbers as shown above: ")) #To Perform operation input enter by user
    list1.printList()
    if opp<=8:
        linkedlist_opp()
        valuefinal = input("\n If you still want to make change type Y else N:")
        value = valuefinal.upper()
    else:
        print("Enter valid number which are given above")



    



    

  