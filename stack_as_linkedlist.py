class  Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
            popped = self.head.data
            self.head = self.head.next
            print("Pop out data is ",popped)

    def printstack(self):
        if self.head is None:
            print("\nstackis empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next
stack1  = stack()
stack1.push(50)
stack1.push(60)
stack1.push(70)
stack1.pop()
stack1.printstack()

