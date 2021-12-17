import queue
# To give number for operation
fun = ["Empty()", "Full()", "Get()", "Get_nowait()", "Put()", "Put_nowait()", "qsize()"]

def operation():
    for i in range(7):
        print("[{}] = {} ".format(i, fun[i]))
def print_queue():
    l = []
    for i in list(q.queue):
        l.append(i)
    print("\ncurrent queue",end=" ")
    return l

def queue_operation():
    if opp == 0:
        print("\nqueue is empty:", q.empty())

    elif opp == 1:
        print("\nqueue is full:",q.full())

    elif opp == 2:
        if q.empty() == True:
            print("\nPlease First enter any element")
        else:
            rm = q.get()
            print("\nelement is: ",rm)
    
    elif opp == 3:
        try:
            q.get_nowait()
            print(print_queue(), end="")
        except:
            print("\nqueue is empty")

    elif opp == 4:
        Choice = int(input("\nSelect how you enter element  \n1) one by one element \n2) multiple element \nSelect anyone "))
        if Choice == 1:
            element = input("\nEnter element which you want to enter in queue:")
            q.put(element)
            print("After element enter queue :",print_queue(), end="")

        elif Choice == 2:
            element = input("\nEnter element which you want to enter in queue(enter with space):")
            if len(list(element.split(" ")))<= max_size:
                for i in element.split():
                    q.put(i)
                print("After element enter queue :",print_queue(), end="")
            else:
                print("\nYou enter more element as compare to maximum size")
        else:
            print("\nPlease select anyone")

    elif opp == 5:
        try:
            element = input("\nEnter element which you want yo enter in queue:")
            q.put_nowait(element)
            print(print_queue(), end="")
        except:
            print("\nqueue is full")

    elif opp == 6:
        size = q.qsize()
        print("\nsize of queue :",size)


if __name__ == "__main__":
    max_size = int(input("\nEnter the size of queue:"))
    q = queue.Queue(maxsize = max_size)
    value = "Y"
    while value == "Y":
        operation()
        print(print_queue(), end="")
        print("\n")
        opp = int(input("\nTo Perform operation enter numbers as shown above:"))  # To Perform operation input enter by user
        if opp <= 6:
            queue_operation()
            valuefinal = input("\n If you still want to make change type Y else N:")
            value = valuefinal.upper()
        else:
            print("\n Enter valid number which are given above")
