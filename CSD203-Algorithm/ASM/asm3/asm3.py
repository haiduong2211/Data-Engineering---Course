#TREE SECTION
import os.path
import json


class BinaryTree:
    def __init__(self, ID=None,name=None,DOB=None,birthplace = None):
        self.left = None
        self.right = None
        self.ID = ID
        self.name = name
        self.DOB = DOB
        self.birthplace = birthplace

#Choice 1 - input from file
    def file_input(self):
        global jsonf
        file_path = input("Please enter the file path: ")
        if os.path.exists(file_path):
            file = open(file_path,'r').read()
            jsonf = json.loads(file)
        else:
            print('->Path is not correct')
            return
        for key in jsonf:
            self.insert(key,jsonf[key][0],jsonf[key][1],jsonf[key][2])
        print("->Input complete")

#Choice 2 - Insert new node to tree    
    def insert(self,ID,name,DOB,birthplace):
    # Compare the new value with the parent node
        if self.ID:
            if self.ID == ID: #ID đã có trong tree  
                print("This ID is taken")
                return
            elif self.ID < ID:
                if self.right is None:
                    self.right = BinaryTree(ID,name,DOB,birthplace)
                else:
                    self.right.insert(ID,name,DOB,birthplace)
            else:
                if self.left is None:
                    self.left = BinaryTree(ID,name,DOB,birthplace)
                else:
                    self.left.insert(ID,name,DOB,birthplace)
        else:
            self.ID = ID
            self.name = name
            self.DOB = DOB
            self.birthplace = birthplace
    
#Update tree vào json list thông qua duyệt cây
    def UpdateTree(self): 
        global jsonf
        jsonf = {}
        if self.ID not in jsonf:
            jsonf[self.ID] = [self.name,self.DOB,self.birthplace]
        if self.left:
            self.left.UpdateTree()
        if self.right:
            self.right.UpdateTree()


#Choice 6 - delite Node base on ID
    def deleteNode(self,key):
        if self is None:
            return self
        #Xóa ID nhỏ hơn node hiện tại    
        elif key < self.ID:
            self.left = self.left.deleteNode(key)
            return self
        #Xóa ID lớn hơn node hiện tại
        elif key > self.ID:
            self.right = self.right.deleteNode(key)
            return self
        else:
            if self.left is None and self.right is None:
                return None
        #Nếu tổn tại 1 trong 2 node con
            if self.left is None:
                temp = self.right
                self = None
                #trả lại nhánh mới đã xóa node cũ
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            #Nếu tồn tại cả 2 nhánh con
            #Tìm node nhất trong nhánh để thay thế
            temp = minvalueNode(self.right)
            self.ID = temp.ID
            #Xóa nút con bé nhất bên nhánh phải
            self.right = self.right.deleteNode(temp.ID)
        return self

#choice 3 - Inorder Travelsal
def inordertravelsal(root): 
    res = []
    if root is not None:
        res = inordertravelsal(root.left)
        res.append(root) #Thêm Node vào danh sách travelsal 
        res = res + inordertravelsal(root.right)
    return res


#Choice 4 - BFS dựa vào queue
def queue_display(root):
    res = []
    if root is None:
        return
    que = [root] #Khởi tạo queue với Node gốc
    res.append(root)
    while len(que) >0:
        cur_node = que.pop(0)
        if cur_node.left is not None:
            que.append(cur_node.left)
            res.append(cur_node.left)
        if cur_node.right is not None:
            que.append(cur_node.right)
            res.append(cur_node.right)
    #In kết quả được append trong res        
    print('{0:7}|{1:15}|{2:15}|{3:7}'.format('ID', 'Name', 'DOB','Birthplace'))
    for node in res:
        print('{0:7}|{1:15}|{2:15}|{3:7}'.format(node.ID,node.name,node.DOB,node.birthplace))


#Choice 5 - Tìm key trong Binarytree
def search(root,key):
    if root is None or root.ID == key:
        return root #Nếu tìm thấy hoặc không có gì thì return giá trị node hiện tại
    elif root.ID < key:
        return search(root.right,key)
    elif root.ID > key:
        return search(root.left,key)
    else:
        return None

#Tìm node nhỏ nhất - dùng thay thế node bị xóa
def minvalueNode(node): 
    current = node
    #Tìm node bên trái nhất của nhánh phải
    while(current.left is not None):
        current = current.left
    return current

def DisplayMenu():
    print("""
+-------------------Menu------------------+
Person Tree:
1. Load the newID from the file.
2. Insert a new Person.
3. Inorder traverse
4. Breadth-First Traversal traverse
5. Search by Person ID
6. Delete by Person ID
Exit:
0. Exit
+-----------------------------------------.+""")
    choice = input('Your choice: ')

#Load Data from file
    if choice == "1":
        BST.file_input()

#Insert new person
    elif choice == "2":
        newID = input("New ID: ")
        newName = input("New Name: ")
        newDOB = input("New DOB: ")
        newBP = input("newBP: ")
        BST.insert(newID,newName,newDOB,newBP)
        BST.UpdateTree
        print("Đã thêm thành công")

#Inorder traverse
    elif choice == "3":
        res = inordertravelsal(BST)
        print('{0:7}|{1:15}|{2:15}|{3:7}'.format('ID', 'Name', 'DOB','Birthplace'))
        for node in res:
            print('{0:7}|{1:15}|{2:15}|{3:7}'.format(node.ID,node.name,node.DOB,node.birthplace))

#Breadth-First Traversal traversal on queue
    elif choice == "4":  
        queue_display(BST)

#Search by Person ID
    elif choice == "5":
        key = input("Please enter search key: ")
        snode = search(BST,key)
        if snode is not None:
            print('{0:7}|{1:15}|{2:15}|{3:7}'.format('ID', 'Name', 'DOB','Birthplace'))
            print('{0:7}|{1:15}|{2:15}|{3:7}'.format(snode.ID,snode.name,snode.DOB,snode.birthplace))
        else:
            print("Cannot Find the ID")

#Delete by Person ID
    elif choice == "6":   
        key = input("Please enter delete key: ")
        BST.deleteNode(key)
        BST.UpdateTree()
#Exit
    elif choice == "0":
        exit()
 
    else:
        print('Vui lòng nhập lại')
    DisplayMenu()

if __name__ == "__main__":
    BST = BinaryTree()
    DisplayMenu()