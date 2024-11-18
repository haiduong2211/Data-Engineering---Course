#Nhập file
fhand = open("diem_trungbinh.txt").readlines()
lisths =[]
dtb_chuan = {}
xep_loai = {}
bangdiemtb  = {}

monhoc = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]
#Tạo bảng điểm trung bình theo dạng dictionary
for line in fhand:
    if line.startswith("Ma"): #Loại line là tiêu đề
        continue
    else:
        linehs = line.split(";") #Split điểm của từng môn theo dấu ";"
        lisths.append(linehs[0]) #Tạo danh sách học sinh
        listdiem = linehs[1:] #Tạo danh sách điểm của từng line (Dạng str)
        listdiemnew =[]
        for i in listdiem:
             newi = i.strip()
             listdiemnew.append(float(newi))
        bangdiemhs = dict(zip(monhoc,listdiemnew)) #Match điểm vào từng môn học
        bangdiemtb[linehs[0]] = bangdiemhs

#Hàm xếp loại học sinh
def xeploai_hocsinh(dtb_chuan):
    for i in lisths:
        dtb_chuan[i] = ((bangdiemtb[i]["Toan"]+bangdiemtb[i]["Ly"]+bangdiemtb[i]["Hoa"])*2 + bangdiemtb[i]["Sinh"]+bangdiemtb[i]["Van"]+bangdiemtb[i]["Anh"]+bangdiemtb[i]["Su"]+bangdiemtb[i]["Dia"])/11.0
        bangdiemhs = bangdiemtb[i]

        #Điểm tối thiểu trong nhóm môn
        for x in bangdiemhs:
            diemmin = min(list(bangdiemhs.values()))

        #Điều kiện xếp loại học sinh
        if dtb_chuan[i] > 9 and diemmin >= 8:
            xep_loai[i] = "Xuat sac"
        elif dtb_chuan[i] > 8 and diemmin >= 6.5:
            xep_loai[i] = "Gioi"
        elif dtb_chuan[i] > 6.5 and diemmin >= 5:
            xep_loai[i] = "Kha"
        elif dtb_chuan[i] > 6 and diemmin >= 4.5:
            xep_loai[i] = "TB kha"
        else:
            xep_loai[i] = "TB"
    return xep_loai

#Hàm xếp loại thi đại học
def xeploai_thidaihoc_hocsinh(bangdiemtb):
    xeploai_dh = {}
    for i in lisths:
        listxeploai = []

        #Khoi A
        dtbkhoiA = (bangdiemtb[i]["Toan"]+bangdiemtb[i]["Ly"]+bangdiemtb[i]["Hoa"])
        if dtbkhoiA >=24:
            listxeploai.append(1)
        elif dtbkhoiA >=18:
            listxeploai.append(2)
        elif dtbkhoiA >=12:
            listxeploai.append(3)
        else:
            listxeploai.append(4)

        #Khoi A1
        dtbkhoiA1 = (bangdiemtb[i]["Toan"]+bangdiemtb[i]["Ly"]+bangdiemtb[i]["Anh"])
        if dtbkhoiA1 >=24:
            listxeploai.append(1)
        elif dtbkhoiA1 >=18:
            listxeploai.append(2)
        elif dtbkhoiA1 >=12:
            listxeploai.append(3)
        else:
            listxeploai.append(4)

        #Khoi B:
        dtbkhoiB = (bangdiemtb[i]["Toan"]+bangdiemtb[i]["Hoa"]+bangdiemtb[i]["Sinh"])
        if dtbkhoiB >=24:
            listxeploai.append(1)
        elif dtbkhoiB >=18:
            listxeploai.append(2)
        elif dtbkhoiB >=12:
            listxeploai.append(3)
        else:
            listxeploai.append(4)

        #Khoi C
        dtbkhoiC = (bangdiemtb[i]["Van"]+bangdiemtb[i]["Su"]+bangdiemtb[i]["Dia"])
        if dtbkhoiC >=21:
            listxeploai.append(1)
        elif dtbkhoiC >=15:
            listxeploai.append(2)
        elif dtbkhoiC >=12:
            listxeploai.append(3)
        else:
            listxeploai.append(4)
            
        #Khoi D
        dtbkhoiD = (bangdiemtb[i]["Toan"]+bangdiemtb[i]["Van"]+bangdiemtb[i]["Anh"])
        if dtbkhoiD >=21:
            listxeploai.append(1)
        elif dtbkhoiD >=15:
            listxeploai.append(2)
        elif dtbkhoiD >=12:
            listxeploai.append(3)
        else:
            listxeploai.append(4)
        xeploai_dh[i] = listxeploai
    return xeploai_dh

#Hàm main
def main():
    newf = open("danhgia_hocsinh.txt","w")
    newf.write("Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D\n")
    datahs = {}
    for i in lisths:
        newf.write(i+";"+ str(xeploai_hocsinh(dtb_chuan)[i])+";"+";".join(str(v) for v in xeploai_thidaihoc_hocsinh(bangdiemtb)[i])+"\n")
    print("Đã xuất file danhgia_hocsinh.txt")
main()
