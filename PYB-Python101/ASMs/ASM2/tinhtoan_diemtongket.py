fhand = open("diem_chitiet.txt").readlines()
bangdiem = {}
lisths = []
monhoc = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]

#Xử lý dữ liệu bảng điểm thành dạng dict = {"hs1":{"Toan":(9,8,7,6),"Ly":(8,8,8,8),...},{...},{...}}
#Check từng line
for line in fhand:
    if line.startswith("Ma"): #Loại line là tiêu đề
        continue
    else:
        linehs = line.split(";") #Split điểm của từng môn theo dấu ";"
        lisths.append(linehs[0]) #Tạo danh sách học sinh
        listdiem = linehs[1:] #Tạo danh sách điểm của từng line (Dạng str)
        listdiemnew =[]
        #Chuyển điểm dạng str thành tupple
        for i in listdiem:
            newi = i.strip().split(",")
            for x in range(0,len(newi)):
                newi[x] = int(newi[x])
            newi = tuple(newi)
            #Tạo list điểm đã xử lý format
            listdiemnew.append(newi)
        bangdiemhs = dict(zip(monhoc,listdiemnew)) #Match điểm vào từng môn học
        bangdiem[linehs[0]] = bangdiemhs #Match dict môn học và điểm vào từng học sinh
#print(bangdiem)

bangdiemtb ={}
#Hàm tính và tạo ra dictionary chứa điểm trung bình của từng môn
def tinhdiem_trungbinh(bangdiem):
    for n in lisths: #Xét từng học sinh
        bangdiemtbhs ={}
        for mon in monhoc: #xét từng môn học
            #Trường hợp môn tự nhiên và môn xã hội
            if len(bangdiem[n][mon]) == 4:
                tbmon = round(0.05*bangdiem[n][mon][0] + 0.1*bangdiem[n][mon][1] + 0.15*bangdiem[n][mon][2] + 0.7*bangdiem[n][mon][3],2)
            else:
                tbmon = round(0.05*bangdiem[n][mon][0] + 0.1*bangdiem[n][mon][1] + 0.1*bangdiem[n][mon][2] + 0.15*bangdiem[n][mon][3] +0.6*bangdiem[n][mon][4],2)
            bangdiemtbhs[mon] = tbmon
        bangdiemtb[n] = bangdiemtbhs
    return bangdiemtb
bangdiemtb = tinhdiem_trungbinh(bangdiem)
#print(bangdiemtb)


#Hàm lưu điểm trung bình
def luudiem_trungbinh(bangdiem):
    fw = open("diem_trungbinh.txt","w")
    fw.write(fhand[0])
    for n in lisths:
        tempstr = str(n)
        for mon in monhoc:
            tempstr += ";" + str(bangdiemtb[n][mon])
        fw.write(tempstr+"\n")
    print('Đã lưu file diem_chitiet.txt')

#Hàm main 
def main():
    tinhdiem_trungbinh(bangdiem)
    luudiem_trungbinh(bangdiem)
    print(open("diem_trungbinh.txt").read())
main()
