import math
#Nhập tọa độ các điểm
try:
    Ax = int(input("Nhập tọa độ x điểm A: "))
    Ay = int(input("Nhập tọa độ y điểm A: "))
    Bx = int(input("Nhập tọa độ x điểm B: "))
    By = int(input("Nhập tọa độ y điểm B: "))
    Cx = int(input("Nhập tọa độ x điểm C: "))
    Cy = int(input("Nhập tọa độ y điểm C: "))
    triABC = [Ax,Ay,Bx,By,Cx,Cy]
except:
    #Check định dạng nhập
    print("Vui lòng nhập đầy đủ tọa độ các điểm")
    quit()
#Check xem các tọa độ có khác nhau không
if (Ax == Bx and Ay == By) or (Ax == Cx and Ay == Cy) or (Bx == Cx and By == Cy):
    print("Vui lòng nhập các tọa độ khác nhau")
    quit()
#Xét 3 điểm có thẳng hàng
def kiemtra_tamgiac(triABC):
    if  (Ax - Bx)*(Ay - Cy) == (Ax - Cx)*(Ay - By):
        return False
        #quit()
    elif (Ax - Bx)*(Ay - By)*(Ax - Cx)==0 and (Ax == Bx == Cx or Ay == By == Cy):
        return False
        #quit()
    else:
        return True

#Hàm tính độ dài các cạnh, góc của tam giác ABC
def goccanh_tamgiac(triABC):
#Tính Độ dài các cạnh
    AB = math.sqrt((Ax - Bx)**2 + (Ay - By)**2)
    BC = math.sqrt((Bx - Cx)**2 + (By - Cy)**2)
    CA = math.sqrt((Cx - Ax)**2 + (Cy - Ay)**2)
#Tính các góc của tam giác từ các cạnh
    rA = math.degrees(math.acos((AB**2 + CA**2 - BC**2)/(2*AB*CA)))
    rB = math.degrees(math.acos((AB**2 + BC**2 - CA**2)/(2*AB*BC)))
    rC = math.degrees(math.acos((BC**2 + CA**2 - AB**2)/(2*BC*CA)))
#Hàm trả về góc cạnh tam giác ABC làm tròn đến số thập phân thứ 2
    return round(AB,2),round(BC,2),round(CA,2),round(rA,2),round(rB,2),round(rC,2)
AB = goccanh_tamgiac(triABC)[0]
BC = goccanh_tamgiac(triABC)[1]
CA = goccanh_tamgiac(triABC)[2]
rA = goccanh_tamgiac(triABC)[3]
rB = goccanh_tamgiac(triABC)[4]
rC = goccanh_tamgiac(triABC)[5]
#Xét tam giác
def xet_tamgiac(triABC):
    #Tam giác đều khi 3 cạnh bằng nhau (Hoặc 3 góc bằng nhau)
    if AB == BC == CA:
        print("ABC là tam giác đều")
    #Tam giác cân khi có 2/3 cạnh bằng nhau
    elif rA == rB or rB == rC or rA ==rC:
        #Xét các điều kiện tam giác cân vuông/Tam giác cân tù
        if rA == 90:
            print("ABC là tam giác vuông cân tại đỉnh A")
        elif rB == 90:
            print("ABC là tam giác vuông cân tại đỉnh B")
        elif rC ==90:
            print("ABC là tam giác vuông cân tại đỉnh C")
        elif rA > 90:
            print("ABC là tam giác tù và cân tại đỉnh A")
        elif rB > 90:
            print("ABC là tam giác tù và cân tại đỉnh B")
        elif rC > 90:
            print("ABC là tam giác tù và cân tại đỉnh C")
        elif rA == rB:
            print("ABC là tam giác cân tại đỉnh C")
        elif rB == rC:
            print("ABC là tam giác cân tại đỉnh A")
        else:
            print("ABC là tam giác cân tại đỉnh B")
    #Tam giác không đều cân ==> Xét điều kiện tam giác vuông/tù
    elif rA == 90:
        print("ABC là tam giác vuông tại đỉnh A")
    elif rB == 90:
        print("ABC là tam giác vuông tại đỉnh B")
    elif rC == 90:
        print("ABC là tam giác vuông tại đỉnh C")
    elif rA > 90:
        print("ABC là tam giác tù tại đỉnh A")
    elif rB > 90:
        print("ABC là tam giác tù tại đỉnh B")
    elif rC > 90:
        print("ABC là tam giác tù tại đỉnh C")
    #Nếu không thỏa điều kiện thì là tam giác thường
    else:
        print("ABC là tam giác thường")

#Tính diện tích tam giác
def dientich_tamgiac(triABC):
    p = (AB+BC+CA)/2
    SABC = math.sqrt(p*(p-AB)*(p-BC)*(p-CA))
    return round(SABC,2)

SABC = dientich_tamgiac(triABC)
#Tính đường cao từ các đỉnh của tam giác
def duongcao_tamgiac(triABC):
    dcA = SABC/BC
    dcB = SABC/CA
    dcC = SABC/AB
    dcABC = [round(dcA,2),round(dcB,2),round(dcC,2)]
    return dcABC
dcABC = duongcao_tamgiac(triABC)

#Hàm tính trung tuyến của tam giác
def trungtuyen_tamgiac(triABC):
    trongtam_x = (Ax + Bx + Cx)/3
    trongtam_y = (Ay + By + Cy)/3
    #Gọi G là trọng tâm của tam giác
    G = [trongtam_x,trongtam_y]
    AG = math.sqrt((Ax - G[0])**2 + (Ay - G[1])**2)
    BG = math.sqrt((Bx - G[0])**2 + (By - G[1])**2)
    CG = math.sqrt((Cx - G[0])**2 + (Cy - G[1])**2)
    return [round(AG,2),round(BG,2),round(CG,2)]

def tam_tamgiac(triABC):
    #Gọi G[Gx.Gy] là trọng tâm tam giác ABC
    Gx = (Ax + Bx + Cx)/3
    Gy = (Ay + By + Cy)/3
    #Gọi H[Hx,Hy] là trực tâm
    #Xét điều kiện tam giác vuông, trực tâm là tọa độ góc vuông
    if rA == 90:
        Hx = Ax
        Hy = Ay
    elif rB == 90:
        Hx = Bx
        Hy = By
    elif rC == 90:
        Hx = Cx
        Hy = Cy
    else:
        #y = kx + m, với
        #hệ số góc AB,BC
        try:
            kAB = (By - Ay)/(Bx - Ax)
            kBC = (Cy - By)/(Cx - Bx)
            #hệ số góc đường cao từ đỉnh C và A
            kCH = -1/kAB
            kAH = -1/kBC
            #kCH = (Hy - Cy)/(Hx - Cx)
            #kAH = (Hy - Ay)/(Hx - Ax)
            Hx = (Cy - Ay + kAH*Ax - kCH*Cx)/(kAH - kCH)
            Hy = kAH * (Hx - Ax) + Ay
        except:
            try:
                kAB = (By - Ay)/(Bx - Ax)
                kCA = (Ay - Cy)/(Ax - Cx)
                #hệ số góc đường cao từ đỉnh C và B
                kCH = -1/kAB
                kBH = -1/kCA
                Hx = (Cy - By + kBH*Bx - kCH*Cx)/(kBH - kCH)
                Hy = kBH * (Hx - Bx) + By
            except:
                kBC = (Cy - By)/(Cx - Bx)
                kCA = (Ay - Cy)/(Ax - Cx)
                #hệ số góc đường cao từ đỉnh B và A
                kAH = -1/kBC
                kBH = -1/kCA
                Hx = (Ay - By + kBH*Ax - kAH*Ax)/(kBH - kAH)
                Hy = kBH * (Hx - Bx) + By
    return [round(Gx,2),round(Gy,2),round(Hx,2),round(Hy,2)]

def giaima_tamgiac(triABC):
    if kiemtra_tamgiac(triABC) == True:
        print("A,B,C hợp thành một tam giác")
    else:
        print("A,B,C không hợp thành một tam giác")
        quit()
    #So do co ban cua tam gic
    print("1. Số đo cơ bản của tam giác:")
    print(" Chiều dài cạnh AB:",goccanh_tamgiac(triABC)[0])
    print(" Chiều dài cạnh BC:",goccanh_tamgiac(triABC)[1])
    print(" Chiều dài cạnh CA:",goccanh_tamgiac(triABC)[2])
    print(" Góc A:",goccanh_tamgiac(triABC)[3])
    print(" Góc B:",goccanh_tamgiac(triABC)[4])
    print(" Góc C:",goccanh_tamgiac(triABC)[5])
    xet_tamgiac(triABC)
    print("2. Diện tích tam giác ABC:",dientich_tamgiac(triABC))
    print("3.Số đo nâng cao của tam giác ABC:")
    print(" Độ dài đường cao từ đỉnh A:",duongcao_tamgiac(triABC)[0])
    print(" Độ dài đường cao từ đỉnh B:",duongcao_tamgiac(triABC)[1])
    print(" Độ dài đường cao từ đỉnh C:",duongcao_tamgiac(triABC)[2])
    print(" Khoảng cách đến trọng tâm từ đỉnh A:",trungtuyen_tamgiac(triABC)[0])
    print(" Khoảng cách đến trọng tâm từ đỉnh B:",trungtuyen_tamgiac(triABC)[1])
    print(" Khoảng cách đến trọng tâm từ đỉnh C:",trungtuyen_tamgiac(triABC)[2])
    print("4.Tọa độ một số điểm đặc biệt của tam giác ABC:")
    print(" Tọa độ trọng tâm:",tam_tamgiac(triABC)[0:2])
    print(" Tọa độ trực tâm:",tam_tamgiac(triABC)[2:4])
giaima_tamgiac(triABC)
