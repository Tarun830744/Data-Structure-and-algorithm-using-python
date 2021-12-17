class  Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self,data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            data1= self.head.data
            self.head = self.head.next
            print("dequeue data is ",data1)

    def printqueue(self):
        if self.head is None:
            print("\nqueue is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

queue1 = Queue()
queue1.enqueue(50)
queue1.enqueue(60)
queue1.enqueue(70)
queue1.dequeue()
queue1.printqueue()




