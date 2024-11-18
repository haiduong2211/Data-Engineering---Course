import sys
import xdrlib

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right: #Nếu có 1 phần tử thì return phần tử đó
        return a[left]
    #write your code here
    else:
        mid = int((left+right)/2) 
        rleft = get_majority_element(a, left,mid)
        rright = get_majority_element(a,mid,right)

        if rleft == rright and rleft !=-1: #Phần tử đa số của cả 2 dãy
            return rleft
        elif rleft !=-1 and rright ==-1: #Phần tử đa số của dãy bên trái
            return rleft
        elif rright !=-1 and rleft ==-1: #Phần tử đa số của dãy phải
            return rright
        else: #trường hợp không phân định được cả 2 dãy đa số thì bắt đầu phép đếm
            cleft = 0
            cright = 0
            for j in a[left:right]:
                if j == rleft:
                    cleft +=1
                if j == rright:
                    cright+=1
            if cleft > cright:
                return rleft
            elif cright > cleft:
                return rright
    return -1

if __name__ == '__main__':
    n = int(input("n: "))
    a = []
    for i in range(n):
        a.append(int(input()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)


