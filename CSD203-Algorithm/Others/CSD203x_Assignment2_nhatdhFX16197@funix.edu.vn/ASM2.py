#khơi tạo danh sách
class Node:
    def __init__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None
#Lớp MyList chứa thông tin và hành vi cơ bản của một danh sách móc nối
class MYlist:
    def __init__(self):
        self.dau = None 
        self.duoi = None
    #hiển thị ra màng hình
    def hien_thi(self):
        stt = 0
        hien_tai = self.dau
        kq = []
        while hien_tai != None:
            stt +=1
            if stt == 1:
                kq.append(hien_tai.gia_tri)
            else:
                kq.append(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        for i in kq:
            print( "".join(i))
    #thêm sản phẩm
    def them(self, gia_tri):
        nut = Node(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi =nut
    #tìm kiếm
    def tim_kiem(self,gia_tri):
        hien_tai = self.dau
        vi_tri = 0
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            hien_tai = hien_tai.nut_ke_tiep
            vi_tri += 1
        #không tìm thấy
        if hien_tai == None:
            print("ID is not in the dataset!")
        #tìm thấy
        else:
            print(hien_tai)
    #Delete
    def xoa(self,gia_tri):
        hien_tai = self.dau
        truoc = None
        while hien_tai != None and hien_tai.gia_tri != gia_tri:
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        #tìm thấy
        if hien_tai != None:
            #nó là phần tử đầu
            if hien_tai == self.dau and hien_tai == self.duoi:
                self.dau = self.duoi = None
            elif hien_tai == self.dau:
                #xóa phần tử đầu nhưng không duy nhất
                self.dau = self.dau.nut_ke_tiep
            elif hien_tai == self.duoi:
                #xóa phần tử duôi nhưng không duy nhất
                truoc.nut_ke_tiep = None
                self.duoi = truoc
            else:
                #xóa giữa
                truoc.nut_ke_tiep = hien_tai.nut_ke_tiep
            print(hien_tai)
            del hien_tai
    #stack "vào sau ra trước"
    def stack(self):
        link = MYlist()
        stac = [link.hien_thi()]
        return stac.reverse()
    #queue " vào trước ra trước"
    def queue(self):
        link = MYlist()
        from queue import Queue
        q = Queue(-1)
        q.put(link.hien_thi())
        while not q.empty():
            gt = q.get()
            print(gt)


DS_ID = []
#chọn 1
def one():
    global DS_ID
    temp = input("Please enter the find path: ")
    #kiểm tra đường link
    import os           
    if os.path.exists(temp) == True:            
            print("The file is loaded successfully!")
            file2 = open(temp,"r").readlines()
            for line in file2:
                if line.startswith("ID"):
                    continue
                else:
                    line = line.strip().split()
                    DS_ID.append(line)               
    else :
           print("File-path is not correct!")
#chọn 2
def two():
    global DS_ID
    new_san_pham = []
    ID = input("Please enter the new product ID:")
    for i in DS_ID :
        if i[0] == ID:
            print("Duplicate ID")
            main()
    name = input("Please enter the product's name:")
    quantity = input("Please enter the product's quantity:")
    price = input("Please enter the product's price:")
    new_san_pham.append(ID)
    new_san_pham.append("|")
    new_san_pham.append(name)
    new_san_pham.append("|")
    new_san_pham.append(quantity)
    new_san_pham.append("|")
    new_san_pham.append(price)
    print(new_san_pham)
    DS_ID.append(new_san_pham)
    print(DS_ID)
#chọn 3
def three():
    global DS_ID
    link = MYlist()
    print("ID |  Title   | Quantity | price")
    for i in DS_ID:
        link.them(i)
    link.hien_thi()
#chọn 4
def fore():
    global DS_ID
    temp = input("Please enter the output path: ")
    file2 = open(temp,"w")
    file2.write("ID |  Title   | Quantity | price\n")
    for i in DS_ID:
        file2.write("".join(i) + "\n")
    file2.close()
    import time
    print("Saving...")
    time.sleep(2)
    print("The file is saved successfully!")
#chọn 5
def five():
    global DS_ID
    temp = input("Please enter the ID:")
    print("ID |  Title   | Quantity | price")
    cout = 0
    for i in DS_ID:
        if i[0]==temp:
            cout +=1
            print("".join(i))
    if cout == 0:
        print("ID is not in the dataset!")
#chọn 6
def Six():
    global DS_ID
    temp = input("Please enter the ID: ")
    print("ID |  Title   | Quantity | price")
    cout = 0
    for i in DS_ID:
        if i[0]==temp:
            print("".join(i))
            cout +=1
            DS_ID.remove(i)
            print("The product is removed from the dataset successfully!")
    if cout == 0:
        print("ID is not in the dataset!")
#chọn 7
def Seven():
    global DS_ID
    print("ID |  Title   | Quantity | price")
    DS = sorted(DS_ID)
    print(DS_ID)
    for i in DS:
        print("".join(i))
#chọn 8
def eight():
    global DS_ID
    temp = input("Please enter the ID:")
    print("ID |  Title   | Quantity | price")
    cout = 0
    for i in DS_ID:
        if i[0] == temp:
            cout +=1
            n = "".join(i)
            n = n.split("|")
            print("|".join(n))
            b = bin(int(n[2]))
            print(f"Convert quantity to binary: {b[2:]}")
            print("The product is removed from the dataset successfully!")
    if cout == 0:
        print("ID is not in the dataset!")
#chon9
#stack
def stack():
    global DS_ID
    print("ID |  Title   | Quantity | price")
    DS_ID.reverse()
    for i in DS_ID :
        print("".join(i))
#chon 10
#Queue
def Queue():
    global DS_ID
    print("ID |  Title   | Quantity | price")
    link = MYlist()
    from queue import Queue
    q = Queue(-1) #max size
    DS_ID.reverse() #đề danh sách giống với lúc đầu nhập vào
    for i in DS_ID:
        q.put(i)
        while not q.empty():
            gt = q.get()
            print("".join(gt))
#hàm main
def main():
    print("+-------------------Menu------------------+")
    choice = input("""        1. Load data from file and display
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
+-----------------------------------------.+
        Enter:""")
    if choice == "1":
        print("Choice 1: Load data from file and display")
        one()
        main()
    if choice == "2":
        print("Choice 2: Input & add to the end")
        two()
        main()
    if choice == "3":
        print("Choice 3: Display data")
        three()
        main()
    if choice == "4":
        print("Choice 4: Save product list to file")
        fore()
        main()
    if choice == "5":
        print("Choice 5: Search by ID")
        five()
        main()
    if choice == "6":
        print("Choice 6: Deleted by ID")
        Six()
        main()
    if choice == "7":
        print("Choice 7: Sorted by ID")
        Seven()
        main()
    if choice == "8":
        print("Choice 8: Convert to Binary")
        eight()
        main()
    if choice == "9":
        print("Choice 9: Load to stack and display")
        stack()
        main()
    if choice == "10":
        print("Choice 10: Load to queue and display")
        Queue()
        main()
    if choice == "0":
        exit()
    else:
        print("No item")
        main()
if __name__=="__main__":
    main()