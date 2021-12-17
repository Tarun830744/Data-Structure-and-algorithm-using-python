stack_list= ["d","e","g","a","r"]
fun = ["Insert()","Append()","Pop()","Remove()","Index()","Count()","extend()","Empty()","Sort()","Search()","Reverse()","clear()"]

# To give number for operation
def operation():
    for i in range(12):
        print("[{}] = {} ".format(i,fun[i]))

def stack_list_oper():

    #----------------To perform insert operation------------------------
    if opp ==0: 
        in_index = int(input("\n First Enter Index number :"))
        in_value = input("\n Enter element which you want to insert :")
        stack_list.insert(in_index, in_value)
        print("\n After insert stack list :",stack_list)
    
    # ---------------To perform append operation------------------------
    elif opp==1:
        ap_value = input("\n Enter Element which you want to append :")
        stack_list.append(ap_value)
        print("\n After append stack list :",stack_list)
            
    #----------------- To perform pop operation----------------------------
    elif opp==2:
        pop_value = int(input("\n Enter index number of element which you want to pop up:"))
        stack_list.pop(pop_value)
        print("\n After pop operation stack list:",stack_list)

    #------------------To perform remove operation-----------------------
    elif opp==3:
        rm_value = input("\n Enter Element which you want to remove in stack list :")
        stack_list.remove(rm_value)
        print("\n After remove stack list :",stack_list)

    #------------------ To find index number operation-------------------------
    elif opp==4:
        in_num = input("\n Enter element which are in stack list to know there index number :")
        x = stack_list.index(in_num)
        print("\n Index number of {} is {}".format(in_num,x))

    # ---------------------To perform count operation--------------------------
    elif opp==5:
        co_value = input("\n Enter element which you want to count :")
        count_stack= stack_list.count(co_value)
        print("\n {} in stack list is {} times".format(co_value,count_stack))
              
    #-------------------- To perform extend operation--------------------------
    elif opp ==6:
        l = []
        ex_ele = input("\n Enter element which you want to extend in stack list one by one using ',':")
        for i in ex_ele.split(','):
            l.append(i)
        stack_list.extend(l)
        print("\n Extended stack list:",stack_list)

    #--------------------To check list is empty or not--------------------------
    elif opp==7:
        empty = len(stack_list)
        if empty ==0:
            print("\n stack list is empty")
        else:
            print("\n they have some element")

    #---------------------To perform sorting operation------------------------------
    elif opp ==8:
        stack_list.sort()
        print("\n After sorting stack list :",stack_list)

    #---------------------To perform search operation----------------------
    elif opp==9:
        search = input("\n Enter a element which you want to search :")
        print("\n",search in stack_list)

    # --------------------To perform reverse operation---------------------------   
    elif opp==10:
        stack_list.reverse()
        print("\n Reverse stack list :",stack_list)
    
    #---------------------To perform clear operation----------------------------
    elif opp==11:
        stack_list.clear()
        print("\n",stack_list)

value ="Y"
while value=="Y":
    operation()
    opp = int(input("\n To Perform operation enter numbers as shown above: ")) #To Perform operation input enter by user
    print("\n",stack_list)
    if opp<=11:
        stack_list_oper()
        valuefinal = input("\n If you still want to make change type Y else N:")
        value = valuefinal.upper()
    else:
        print("Enter valid number which are given above")


        
