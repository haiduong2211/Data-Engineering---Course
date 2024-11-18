import os.path
import json

#Class Node để quản lý thông tin và hành vi của mỗi lớp trong danh sách
class Node:
    def __init__(self, ID,Title,quantity,price):
        self.ID = ID
        self.Title = Title
        self.quantity = quantity
        self.price = price
        self.nextval = None

#Class MyList chứa thông tin và hành vi cơ bản của một danh sách móc nối
class MyList():
    def __init__(self):
        self.headval = None
        self.nextval = None

    def check_valid_input(self,input):
        cur_node = self.headval
        while cur_node:
            if cur_node.ID == input:
                return True
            cur_node = cur_node.nextval
        return False

    #Choice1 - Nhập inputfile
    def file_input(self):
        global jsonf
        #file_path = r"C:\Users\Duong Nguyen\Desktop\DE\Algorithm\ASM\asm2\input.json"
        file_path = input("Please enter the file path: ")
        if os.path.exists(file_path):
            file = open(file_path,'r').read()
            jsonf = json.loads(file)
        else:
            print('Path is not correct!') 
            DisplayMenu()
        for key in jsonf:
            self.lappend(key,jsonf[key][0],jsonf[key][1],jsonf[key][2])
        print('The file is loaded successfully!')

    #Choice2 - append file
    def lappend(self,newID,newTitle,newQuantity,newPrice):
        NewNode = Node(newID,newTitle,newQuantity,newPrice)
        if self.headval is None:
            self.headval = NewNode
            return
        lastNode = self.headval
        while lastNode.nextval:
            lastNode = lastNode.nextval
        lastNode.nextval = NewNode

    #Choice3
    def print_list(self):
        print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
        printval = self.headval
        while  printval is not None:
            print('{0:7}|{1:15}|{2:10}|{3:7}'.format(printval.ID,printval.Title,printval.quantity,printval.price))
            printval = printval.nextval

    #Choice4
    def save_to_file(self):
        dic = {}
        save_path = input('Please enter output path: ')
        file = open(save_path,'w')
        cur_ID = self.headval
        if self.headval is None:
            ans = input('You are saving a BLANK FILE, do you want to continue?(Y/N) ')
            if ans == 'N' or ans == 'n':
                DisplayMenu()
                
        while cur_ID:
            dic[cur_ID.ID] = [cur_ID.Title,cur_ID.quantity,cur_ID.price]
            cur_ID = cur_ID.nextval
        write_json = json.dumps(dic)
        file.write(write_json)
        print('File saved successfully!')

    #Choice5
    def search_ID(self):
        SID = input("Please enter the ID: ")
        if not self.check_valid_input(SID):
            print('ID is not in Dataset ')
            return
        cur_node = self.headval
        count = 0
        while cur_node:
            if cur_node.ID == SID:
                if count == 0:
                    print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
                print('{0:7}|{1:15}|{2:10}|{3:7}'.format(cur_node.ID,cur_node.Title,cur_node.quantity,cur_node.price))
                count +=1
            cur_node = cur_node.nextval
        if count == 0:
            print("ID is not in Dataset")

    #Choice6
    def delete_ID(self):
        DID = input("please enter the ID: ")
        if not self.check_valid_input(DID):
            print('ID is not in Dataset ')
            return
        temp_node = self.headval
        if temp_node is not None: #If the headval is the key to be deleted
            if temp_node.ID == DID:
                print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
                print('{0:7}|{1:15}|{2:10}|{3:7}'.format(temp_node.ID,temp_node.Title,temp_node.quantity,temp_node.price))
                self.headval = temp_node.nextval
                temp_node = None
                print('The product is deleted successfully!')
                return
        
        while temp_node is not None:
            if temp_node.ID == DID:
                break
            prev_node = temp_node
            temp_node = temp_node.nextval
        
        if temp_node == None:
            print('The ID is not in dataset')
            return
        print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
        print('{0:7}|{1:15}|{2:10}|{3:7}'.format(temp_node.ID,temp_node.Title,temp_node.quantity,temp_node.price))
        prev_node.nextval = temp_node.nextval
        temp_node = None
                    
                    
    #Choice7
    def sorted_ID(self):
        try:
            templist = sorted(jsonf)
        except NameError:
            print('Emty Dataset')
            return
        print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
        for key in templist:
            cur_node = self.headval
            while cur_node is not None:
                if cur_node.ID == key:
                    print('{0:7}|{1:15}|{2:10}|{3:7}'.format(cur_node.ID,cur_node.Title,cur_node.quantity,cur_node.price))
                    break
                cur_node = cur_node.nextval
                    
    #Choice 8
    def convert_to_binary(self):
        CID = input('Please input the ID: ')
        if not self.check_valid_input(CID):
            print('ID is not in Dataset ')
            return
        cur_node = self.headval
        while cur_node:
            if cur_node.ID == CID:
                print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
                print('{0:7}|{1:15}|{2:10}|{3:7}'.format(cur_node.ID,cur_node.Title,cur_node.quantity,cur_node.price))
                break
            cur_node = cur_node.nextval
        print('Convert Quantity to Binary: ', self.binary_recursion(cur_node.quantity))

    #Hàm đẹ quy chuyển thành nhị phân        
    def binary_recursion(self,n):
        if n == 0:
            return 0
        else:
            b = n%2
            return self.binary_recursion(n//2)*10 + b
#Choice9
def stack_display():
    st = Stack()
    cur_node = ProductList.headval
    while cur_node:
        st.add(cur_node)
        cur_node = cur_node.nextval
    print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))
            
    while st.is_emty() == False:
        cur_node = st.remove()
        print('{0:7}|{1:15}|{2:10}|{3:7}'.format(cur_node.ID,cur_node.Title,cur_node.quantity,cur_node.price))


#Choice10
def queue_display():
    que = Queue()
    cur_node = ProductList.headval
    while cur_node:
        que.add(cur_node)
        cur_node= cur_node.nextval
    print('{0:7}|{1:15}|{2:10}|{3:7}'.format('ID', 'Title', 'Quantity','price'))

    while que.size() > 0:
        cur_node = que.remove()
        print('{0:7}|{1:15}|{2:10}|{3:7}'.format(cur_node.ID,cur_node.Title,cur_node.quantity,cur_node.price))

#-----------------------STACK--------------------------# 
# STACK để chứa các hành vi của stack           
class Stack:
    def __init__(self):
        self.stack = []
    def is_emty(self):
        if len(self.stack) <=0:
            return True
        return False

    def add(self, dataval):
    # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    # Use peek to look at the top of the stack
    def peek(self):
        if len(self.stack) <= 0:
            return None
        return self.stack[-1]

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
#--------------------END-STACK-------------------------#    
#-----------------------QUEUE--------------------------#    
class Queue:
    def __init__(self):
        self.queue = list()

    def add(self,dataval):
    # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False

    def size(self):
        return len(self.queue)

        # Pop method to remove element
    def remove(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in Queue!")

#--------------------END-QUEUE-------------------------#    

def DisplayMenu():
    print("""
+-------------------Menu------------------+
    1. Load data from file and display
    2. Input & add to the end.
    3. Display data
    4. Save product list to file.
    5. Search by ID
    6. Delete by ID
    7. Sort by ID.
    8. Convert to Binary 
    9. Load to stack and display
    10. Load to queue and display.
    Exit:
    0. Exit
+-----------------------------------------.+""")

    choice = input('Your choice: ')
    if choice == "1":
        ProductList.file_input()
    elif choice == "2":
        try:
            newID  = input('NewID: ')
            newTitle = input('NewTitle:')
            newQuantity = int(input('NewQuantity:'))
            newPrice = float(input("NewPrice:"))
        except ValueError:
            print('Please insert the correct format...')
            DisplayMenu()
        ProductList.lappend(newID,newTitle,newQuantity,newPrice)
    elif choice == "3":
        ProductList.print_list()
    elif choice == "4":
        ProductList.save_to_file()
    elif choice == "5":
        ProductList.search_ID()
    elif choice == "6":
        ProductList.delete_ID()
    elif choice == "7":
        ProductList.sorted_ID()
    elif choice == "8":
        ProductList.convert_to_binary()
    elif choice == "9":
        stack_display()
    elif choice =="10":
        queue_display()
    elif choice == "0":
        exit()
    else:
        print('Vui lòng nhập lại')
    DisplayMenu()

if __name__ == "__main__":
    ProductList = MyList()
    DisplayMenu()
