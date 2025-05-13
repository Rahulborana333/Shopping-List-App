
#Shopping List App

#!Menu Section
def Menu():
    print("<SHOPPIN LIST SYSTEM>")
    print("1.ADD ITEM")
    print("2.REMOVE ITEM")
    print("3.SEARCH ITEM")
    print("4.SAVE ITEM")

#!Add Item Function
def Add_item(Shopping_List):
    Item=input("Enter Item Name For Add :")
    Price=int(input("Enter Item Price :"))
    Shopping_List[Item]=Price
    print(f"Item :{Item} Added Succesfully")

#!Remove Item Function
def Remove_item(Shopping_List):
    Item=input("Enter Item Name For Remove :")
    if Item in Shopping_List:
        del Shopping_List[Item]
        print("Item Removed Succesfully!")
    else:
        print("Item Not Found!")

#!Search Item Function
def Search_item(Shopping_List):
    Item=input("Enter Item For Search :")
    if Item in Shopping_List:
        print(f"Item {Item} -{Shopping_List[Item]}")
    else:
        print("Item Not Found!")

#!Save Item In File Function
def Save_item_file(Shopping_List):
    with open("save_item.txt","w") as f:
        for item,price in Shopping_List.items():
            f.write(F"{item}:{price} \n",)
            print("Item Saved Successfully!")
    


#!def Main Function
def Main():
    Shopping_List={}
    while True:
        Menu()
        Choice=int(input("Enter Your Choice :"))
        if Choice==1:
            Add_item(Shopping_List)
        elif Choice==2:
            Remove_item(Shopping_List)
        elif Choice==3:
            Search_item(Shopping_List)
        elif Choice==4:
            Save_item_file(Shopping_List)
        elif Choice==5:
            print("Exiting Shopping List App")
            break
        else:
            print("Invalid Choice !Please Try Again!")
if __name__=="__main__":
    Main()

































































