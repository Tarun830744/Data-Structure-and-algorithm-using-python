from collections import  deque
stack_deque = deque(["d","e","g","a","r"])
fun = ["Insert()","Append()","Appendleft()","Pop()","Popleft()","Remove()","Index()","Count()","Extend()","Extendleft()","Rotate()","Empty()","Sort()","Search()","Reverse()"]

# To give number for operation
def operation():
    for i in range(15):
        print("[{}] = {} ".format(i,fun[i]))

def stack_deque_oper():

    #----------------To perform insert operation------------------------
    if opp ==0: 
        in_index = int(input("\n First Enter Index number :"))
        in_value = input("\n Enter element which you want to insert :")
        stack_deque.insert(in_index, in_value)
        print("\n After insert stack deque :",stack_deque)
    
    # ---------------To perform append operation------------------------
    elif opp==1:
        ap_value = input("\n Enter Element which you want to append :")
        stack_deque.append(ap_value)
        print("\n After append stack deque :",stack_deque)

    # ---------------To perform appendleft operation------------------------
    elif opp==2:
        ap_value = input("\n Enter Element which you want to append left:")
        stack_deque.appendleft(ap_value)
        print("\n After appendleft stack deque :",stack_deque)
      
    #----------------- To perform pop operation----------------------------
    elif opp==3:
        pop_value = int(input("\n Enter index number of element which you want to pop up:"))
        stack_deque.pop(pop_value)
        print("\n After pop operation stack deque :",stack_deque)

    #----------------- To perform popleft operation----------------------------
    elif opp==4:
        pop_value = int(input("\n Enter index number of element which you want to pop left :"))
        stack_deque.popleft(pop_value)
        print("\n After popleft operation stack deque :",stack_deque)


    #------------------To perform remove operation-----------------------
    elif opp==5:
        rm_value = input("\n Enter Element which you want to remove in stack deque :")
        stack_deque.remove(rm_value)
        print("\n After remove stack deque :",stack_deque)

    #------------------ To find index number operation-------------------------
    elif opp==6:
        in_num = input("\n Enter element which are in stack deque to know there index number :")
        x = stack_deque.index(in_num)
        print("\n Index number of {} is {}".format(in_num,x))

    # ---------------------To perform count operation--------------------------
    elif opp==7:
        co_value = input("\n Enter element which you want to count :")
        count_stack= stack_deque.count(co_value)
        print("\n {} in stack deque is {} times".format(co_value,count_stack))
              
    #-------------------- To perform extend operation--------------------------
    elif opp ==8:
        l = []
        ex_ele = input("\n Enter element which you want to extend in stack deque one by one using ',':")
        for i in ex_ele.split(','):
            l.append(i)
        stack_deque.extend(l)
        print("\n Extended stack deque:",stack_deque)

    #-------------------- To perform extent left operation--------------------------
    elif opp ==9:
        l = []
        ex_ele = input("\n Enter element which you want to extend left in stack deque one by one using ',':")
        for i in ex_ele.split(','):
            l.append(i)
        stack_deque.extendleft(l)
        print("\n Extended stack deque:",stack_deque)

    #------------------to perform rotate operation--------------------------
    elif opp==10:
        rotat = int(input("\n Enter a number \n when you Enter negative number it rotation occur to left \n when you Enter posotive number it rotation occur to right :"))
        stack_deque.rotate(rotat)
        print("\n After rotation stack deque :",stack_deque)

    #--------------------To check list is empty or not--------------------------
    elif opp==11:
        empty = len(stack_deque)
        if empty ==0:
            print("\n stack deque is empty")
        else:
            print("\n they have some element")

    #---------------------To perform sorting operation------------------------------
    elif opp ==12:
        stack_deque.sort()
        print("\n After sorting stack deque :",stack_deque)

    #---------------------To perform search operation----------------------
    elif opp==13:
        search = input("\n Enter a element which you want to search :")
        print("\n",search in stack_deque)

    # --------------------To perform reverse operation---------------------------   
    elif opp==14:
        stack_deque.reverse()
        print("\n Reverse stack deque :",stack_deque)
    

value ="Y"
while value=="Y":
    operation()
    opp = int(input("\n To Perform operation enter numbers as shown above: ")) #To Perform operation input enter by user
    print("\n",stack_deque)
    if opp<=11:
        stack_deque_oper()
        valuefinal = input("\n If you still want to make change type Y else N:")
        value = valuefinal.upper()
    else:
        print("Enter valid number which are given above")


        
