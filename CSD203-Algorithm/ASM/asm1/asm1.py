
import fileinput
import os.path
from re import A
import time

#ManualInput
def ManualInput(): #1
    print("Please enter input number of elements: ")
    try:
        n = int(input())
        a = []
        file = open("input.txt",'w')
        print("Please enter input elements: ")
        for i in range(n):
            a.append(float(input()))
    except ValueError:
        print("Vui lòng nhập đúng dạng ký tự")
    for i in range(len(a)):
        if i == len(a)-1:
            string = str(a[i])
        else:
            string = str(a[i])+" "
        file.write(string)
    file.close()

#FileInput (Nhập dữ liệu vào)
def FileInput(): #2
    global a
    #file_path = input("file path: ")
    #file_name = input("File name: ")
    #file1 = os.path.join(file_path,file_name)
    file1 = "C:/Users/Duong Nguyen/Desktop/DE/Algorithm/Asm/asm1/input.txt"
    f = open(file1,'r').readline()
    a = f.split(" ")
    for i in range(len(a)):
        a[i] = float(a[i])
        print(a[i], end = ' ')
    print("\n")
    return a

#Choice 3 - Bubble Sort
def BubbleSort(): #3
    b = list(a)
    for i in range(len(b)-1,1,-1):
        for j in range(0,i):
            if b[j]>b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]
        print(*b, sep = ' ')
    file = open("OUTPUT1.TXT",'w')
    for i in b:
        file.write(str(i) + " ")
    file.close()


def SelectionSort(): #4
    b = list(a)
    for i in range(0,len(b)):
        indexMin = i
        for j in range(i+1,len(b)):
            if b[indexMin] > b[j]:
                indexMin = j
        if i != indexMin:
            b[i],b[indexMin] = b[indexMin],a[i]
        print(*b, sep = ' ')
    file = open("OUTPUT2.TXT",'w')
    for i in b:
        file.write(str(i) + " ")
    file.close()

def InsertionSort(): #5
    b = list(a)
    for i in range(1,len(b)):
        index = i
        value = b[i]
        while (index > 0 and b[index-1]>value):
            b[index] = b[index-1] #Dời số index -1 sang index (vẫn giữ value chưa assign)
            index -=1
        b[index] = value
        print(*b, sep = ' ')
    file = open("OUTPUT3.TXT",'w')
    for i in b:
        file.write(str(i) + " ")
    file.close()


def SearchGreater(): #6
    x = float(input("Nhập số cần tìm: "))
    print("Larger Index: ",end = '')
    b = []
    for i in range(len(a)):
        if a[i] > x:
            b.append(i)
    if not b:
         print("Không có giá trị lớn hơn",x)
    else:
        for i in b:
            print(i, end=' ')
    file = open("OUTPUT4.TXT",'w')
    for i in b:
        file.write(str(i) + " ")
    file.close()


def SearchValue(): #7
    x = float(input("Nhập số so sánh x: "))
    print("Vị trí của số lớn hơn số x: ",end = "")
    return BinarySearch(a,0,len(a)-1,x)

def BinarySearch(a,left,right,x):
    mid = (right + left)//2
    if left == right:
        return "Không có"
    if a[mid] == x:
        return mid
    elif x < a[mid]:
        return BinarySearch(a,left,mid-1,x)
    elif a[mid] < x:
        return BinarySearch(a,mid+1,right,x)
    return mid


def main():
    print('''
+-----------------Menu----------------+
|      1.Manual Input                 |
|      2.File input                   |
|      3.Bubble sort                  |
|      4.Selection sort               |
|      5.Insertion sort               |
|      6.Search > value               |
|      7.Search = value               |
|      0.Exit                         |
+------------------------------------.+''')
    try:
        choice = int(input("Nhập thao tác: "))
    except ValueError:
        print("Vui lòng nhập đúng giá trị! ", end = '')
        main()
    if choice == 1:
        ManualInput()
        main()
    elif choice == 2:
        a = FileInput()
        main()
    elif choice == 3:
        BubbleSort()
        main()
    elif choice == 4:
        SelectionSort()
        main()
    elif choice ==5:
        InsertionSort()
        main()
    elif choice == 6:
        SearchGreater()
        main()
    elif choice == 7:
        print(SearchValue())
        main()
    elif choice == 0:
        exit()
    else:
        print("Vui lòng nhập lại lựa chọn:\n")
        main()
if __name__ == '__main__':
    print(" nhập file input: ")
    a = FileInput()
    main()


