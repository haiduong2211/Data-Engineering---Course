# File thông tin thuế XML
info1 = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7"

#File Phạt muộn JSON
info2 =" https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de"

#Import lib
import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as ET
print("Đang tải dữ liệu thuế và phạt, xin đợi một chút")
print(".....")
file1 = urllib.request.urlopen(info1).read()
data1 = ET.fromstring(file1)
print(".....")
tax_list = data1.findall('tax')
file2 = urllib.request.urlopen(info2).read()
data2 = json.loads(file2)
print("Done extract data")

def create_id_dict():
    id_dict = {}
    try:
        id_dict = json.load(open('employment_data.json','r'))
        return id_dict
    except:
        return id_dict

def create_dep_dict():
    dep_dict = {}
    try:
        dep_dict = json.load(open('department_data.json','r'))
        return dep_dict
    except:
        return dep_dict

#Tạo các class
class Department():
    def __init__(self,department,bonus_salary):
        self.department = department
        self.bonus_salary = bonus_salary


class Employee(Department):
    def __init__(self,id,name,salary_base,working_days,department,working_performance,bonus,late_comming_days,bonus_salary):
        super().__init__(department,bonus_salary)
        self.id = id
        self.name = name
        self.salary_base = salary_base
        self.working_days = working_days
        self.department = department
        self.working_performance = working_performance
        self.bonus = bonus
        self.late_comming_days = late_comming_days

    #Hàm tính lương cho nhân viên
    def tinhluong(self):
        self.salary = (self.salary_base * self.working_days) * self.working_performance
        self.gross_income = self.salary + self.bonus + self.bonus_salary - self.tinhphat()
        self.taxable_income = self.gross_income * 0.895
        #Tính thuế
        for tax in tax_list:
            try:
                if int(tax.find('min').text) <= self.taxable_income/1000000 < int(tax.find('max').text):
                    self.tax_amount = int(tax.find('value').text)/100*self.taxable_income
                    #BaseException
            except KeyError:
                if int(tax.find('min').text) <= self.taxable_income/1000000:
                    self.tax_amount = int(tax.find('value').text)/100*self.taxable_income

        self.net_income = self.taxable_income - self.tax_amount
        return self.net_income

    
    def tinhphat(self):
        for a in data2:
            try:
                if a['min'] <= self.late_comming_days <= a['max']:
                    return a['value']*self.late_comming_days
            except KeyError:
                return a['value']*self.late_comming_days

#Kế thừa từ class Nhân viên
class Manager(Employee):
    def __init__(self,id,name,salary_base,working_days,department,working_performance,bonus,late_comming_days,bonus_salary):
        super().__init__(id,name,salary_base,working_days,department,working_performance,bonus,late_comming_days,bonus_salary)
        self.bonus_salary = bonus_salary*0.1
    def tinhluong(self):
        self.salary = (self.salary_base * self.working_days) * self.working_performance
        self.gross_income = self.salary + self.bonus + self.bonus_salary*1.1 - self.tinhphat() #Manager thêm 10% bonus bộ phận
        self.taxable_income = self.gross_income * 0.895
        #Tính thuế
        for tax in tax_list:
            try:
                if int(tax.find('min').text) <= self.taxable_income/1000000 < int(tax.find('max').text):
                    self.tax_amount = int(tax.find('value').text)/100*self.taxable_income
                    
            except KeyError:
                if int(tax.find('min').text) <= self.taxable_income/1000000:
                    self.tax_amount = int(tax.find('value').text)/100*self.taxable_income
                    
        self.net_income = self.taxable_income - self.tax_amount
        return self.net_income

# CÁC CHỨC NĂNG CỦA CHƯƠNG TRÌNH
#1. Hiển thị danh sách nhân viên
def DSNhanVien():
    id_dict = create_id_dict()
    #iterate qua danh sách
    if bool(id_dict) == False:
        print("Không có dữ liệu nhân viên!")
    else:
        for id in id_dict:
            print("----")
            print("Mã số:",id)
            print("Mã bộ phận:",id_dict[id]['department'])
            print("Họ và tên:",id_dict[id]['name'])
            print("Hệ số lương:","{:,}".format(id_dict[id]['salary_base']),'(VND)')
            print("Số ngày làm việc:",id_dict[id]['working_days'], '(ngày)')
            print("Hệ số hiệu quả:",id_dict[id]['working_performance'])
            print("Thưởng:","{:,}".format(id_dict[id]['bonus']))
            print("Số ngày đi muộn:",id_dict[id]['late_comming_days'])
            print("----")

    backtomain()


#2.Hiển thị danh sách bộ phận
def DSBoPhan():
    dep_dict = create_dep_dict()
    if bool(dep_dict) == False:
        print("Không có dữ liệu phòng ban")
    else:
        for dep in dep_dict:
            print("----")
            print("Mã bộ phận:",dep)
            print("Thưởng bộ phận:","{:,}".format(dep_dict[dep]))
    backtomain()

#3.THÊM NHÂN VIÊN MỚI 
#Nhập dữ liệu
def nhanvienmoi():
    id_dict = create_id_dict()
    dep_dict = create_dep_dict()
    #Nhập mã số NV
    while True:
        id = input("Nhập mã số NV:")
        if id == "":
            print('Bạn không được để trống thông tin này')
        else:
            # Check mã nhân viên
            if bool(id_dict) == False:
                break
            elif id in id_dict:
                print("Mã nhân viên đã tồn tại")
                return main()
            else:
                break
    #CHỨC VỤ
    while True:
        title = input('Vui lòng nhập đúng định dạng (NV/QL)')
        if title == 'NV' or title == 'QL':
            break
        else:
            print('Vui lòng nhập NV hoặc QL')

    #HỌ VÀ TÊN
    while True:
        name = input("Họ và Tên:")
        if name == "":
            print('Bạn không được bỏ trống thông tin này')
        else:
            break
    
    #BỘ PHẬN
    #Mở file lưu trữ department
    try:
        dep_data = open('department_data.json','r')
        dep_dict = json.load(dep_data)
    except FileNotFoundError:
        pass
    except:
        pass

    department = input("Nhập mã bộ phận:")
    if department not in dep_dict:
        print(f'Mã bộ phận chưa tồn tại, tạo mới ... {department}')
        while True:
            try:
                dep_bonus = int(input('Nhập thưởng bộ phận: '))
                if dep_bonus < 0:
                    raise 
                dep_dict[department] = dep_bonus
                
                break
            except ValueError:
                print("Hãy nhập giá trị dưới dạng số")

    #viết data vào file
    dep_data = open('department_data.json','w')
    json.dump(dep_dict,dep_data)
    dep_data.close()
    ### ------Bộ phận-------- ###
    #Thông tin tính lương
    while True:
        try:
            salary_base = int(input("Nhập hệ số lương cơ bản:"))
            working_days = int(input("Nhập số ngày làm việc trong tháng:"))
            working_performance = float(input("Nhập hệ số hiệu quả:"))
            bonus = int(input("Nhập thưởng:"))
            late_comming_days = int(input("Nhập số ngày đi muộn:"))
            break
        except ValueError:
            print('Vui lòng nhập định dạng là số')
        
    #Thêm thông tin vào dict
    info_dict = {}
    info_dict['title'] = title
    info_dict['name'] = name
    info_dict['salary_base'] = salary_base
    info_dict['working_days'] = working_days
    info_dict['department'] = department
    info_dict['working_performance'] = working_performance
    info_dict['bonus'] = bonus
    info_dict['late_comming_days'] = late_comming_days   

    #Thêm ID mới vào id_dict
    id_dict[id] = info_dict
    #Write Dữ liệu được nhập vào file 
    fw = open('employment_data.json','w')
    json.dump(id_dict,fw)
    fw.close()
    print('Đã thêm nhân viên mới')
    backtomain()
    

#4.Xóa nhân viên theo ID
def XoaNV():
    id_dict = create_id_dict()
    while True:
        id_del = input('Nhập mã nhân viên muốn xóa:')
        if id_del == "":
            print("Bạn không được bỏ trống thông tin này")
        else:
            try:
                id_dict.pop(id_del)
                with open('employment_data.json','w') as file:
                    json.dump(id_dict,file)
                print('Đã xóa nhân viên',id_del)
                break
            except KeyError:
                print("Mã nhân viên không tồn tại")
                break
    backtomain()

#5. Xóa bộ phận theo mã bộ phận
def XoaBP():
    id_dict = create_id_dict()
    dep_dict = create_dep_dict()
    while True:
        dep_del = input('Nhập mã bộ phận muốn xóa:')
        if dep_del == "":
            print("Bạn không được bỏ trống thông tin này")
        else:
            dep_list = []
            for k in id_dict:
                dep_list.append(id_dict[k]['department'])
            
            if dep_del in dep_list:
                print("!!!\nKhông thể xóa bộ phận đang có nhân viên")
                return main()
            else:
                try:
                    dep_dict.pop(dep_del)
                    with open('department_data.json','w') as file:
                        json.dump(dep_dict,file)
                    print('Đã xóa bộ phận',dep_del)
                    break
                except KeyError:
                    print("Mã bộ phận không tồn tại")
                    break
    backtomain()

#6.Hiển thị bảng lương
def HienThiBangLuong():
    id_dict = create_id_dict()
    dep_dict = create_dep_dict()
    for k in id_dict:
        if id_dict[k]['title'] == 'NV':
            tempk = Employee(k,id_dict[k]['name'],id_dict[k]['salary_base'],id_dict[k]['working_days'],id_dict[k]['department'],id_dict[k]['working_performance'],id_dict[k]['bonus'],id_dict[k]['late_comming_days'],dep_dict[id_dict[k]['department']])
            print("----")
            print("Mã số nhân viên",k)
            print('thu nhập thực nhận',"{:,}".format(int(round(tempk.tinhluong(),0))),'(VND)')
        else:
            tempk = Manager(k,id_dict[k]['name'],id_dict[k]['salary_base'],id_dict[k]['working_days'],id_dict[k]['department'],id_dict[k]['working_performance'],id_dict[k]['bonus'],id_dict[k]['late_comming_days'],dep_dict[id_dict[k]['department']])
            print("----")
            print("Mã số nhân viên:",k)
            print('thu nhập thực nhận:',"{:,}".format(int(round(tempk.tinhluong(),0))),'(VND)')
    
    backtomain()


#Chỉnh sửa nhân viên   
def ChinhSuaNV():
    id_dict = create_id_dict()
    id_sua = input("Nhập mã nhân viên:")
    
    if id_sua not in id_dict:
        print("Mã nhân viên không tồn tại")
        return
    else:
        #Nhập các dữ liệu chỉnh sửa
        temp  = input("Nhập họ và tên:")
        if temp == "":
            pass
        else:
            id_dict[id_sua]['name'] = temp
        #Sửa chức vụ
        temp = ""
        while True:
            temp = input("Nhập cức vụ (NV/QL):")
            if temp == "":
                break
            elif temp == 'NV' or temp == 'QL':
                id_dict[id_sua]['title'] = temp
                break
            else:
                pass
        #Sửa hệ số lương
        temp = ""
        while True:
            temp = input('Nhập hệ số lương:')
            if temp == "":
                break
            else:
                try:
                    temp = int(temp)
                    if temp < 0:
                        print("Vui lòng nhập đúng định dạng")
                        continue
                    else:
                        id_dict[id_sua]['salary_base'] = temp
                        break           
                except ValueError:
                    pass
        #Sửa số ngày làm việc
        temp = ""
        while True:
            temp = input('Nhập số ngày làm việc:')
            if temp == "":
                break
            else:
                try:
                    temp = int(temp)
                    if temp < 0:
                        print("Vui lòng nhập đúng định dạng")
                        continue
                    else:
                        id_dict[id_sua]['working_days'] = temp
                        break           
                except ValueError:
                    pass
        #Sửa hệ số hiệu quả
        temp = ""
        while True:
            temp = input('Nhập hệ số hiệu quả:')
            if temp == "":
                break
            else:
                try:
                    temp = float(temp)
                    if temp < 0:
                        print("Vui lòng nhập đúng định dạng")
                        continue
                    else:
                        id_dict[id_sua]['working_performance'] = temp
                        break           
                except ValueError:
                    pass
        #Sửa thưởng
        temp = ""
        while True:
            temp = input('Nhập thưởng:')
            if temp == "":
                break
            else:
                try:
                    temp = int(temp)
                    if temp < 0:
                        print("Vui lòng nhập đúng định dạng")
                        continue
                    else:
                        id_dict[id_sua]['bonus'] = temp
                        break           
                except ValueError:
                    pass
        #Sửa số ngày đi muộn
        temp = ""
        while True:
            temp = input('Nhập số ngày đi muộn:')
            if temp == "":
                break
            else:
                try:
                    temp = int(temp)
                    if temp < 0:
                        print("Vui lòng nhập đúng định dạng")
                        continue
                    else:
                        id_dict[id_sua]['late_comming_days'] = temp
                        break           
                except ValueError:
                    pass
    #Chỉnh sửa nhân viên
    fw = open('employment_data.json','w')
    json.dump(id_dict,fw)
    fw.close()
    print('Chỉnh sửa nhân viên thành công')  
    backtomain()

def backtomain():
    back = input(""" #Trở về menu chính (Y) hoặc nhập bất kỳ để thoát: """)
    if back == "Y" or back == 'y':
        main()
    else:
        exit()
#Tạo menu để lựa chọn các chức nămg
def main():
    #ans = input("\n---------------------\n1. Hiển thị danh sách nhân viên.\n2. Hiển thị danh sách bộ phận.\n3. Thêm nhân viên mới.\n4. Xóa nhân viên theo ID.\n5. Xóa bộ phận theo ID.\n6. Hiển thị bảng lương.\n7. Chỉnh sửa nhân viên. \n8. Thoát\n Mời bạn nhập chức năng mong muốn:")
    ans = input("""
    *************************
    1. Hiển thị danh sách nhân viên
    2. Hiển thị danh sách bộ phận
    3. Thêm nhân viên mới
    4. Xóa nhân viên theo ID
    5. Xóa bố phận theo ID
    6. Hiển thị bảng lương
    7. Chỉnh sửa nhân viên
    8. Thoát
    Mời bạn nhập chức năng mong muốn: """)
    if ans == '1':
        print('---Hiển thị danh sách nhân viên---')
        DSNhanVien()
    elif ans == '2':
        print('---Hiển thị danh sách bộ phận---')
        DSBoPhan()
    elif ans == '3':
        print('---Thêm nhân viên mới---')
        nhanvienmoi()
    elif ans == '4':
        print('---Xóa nhân viên theo ID---')
        XoaNV()
    elif ans == '5':
        print('---Xóa bộ phận theo ID---')
        XoaBP()
    elif ans == '6':
        print('---Hiển thị bảng luong---')
        HienThiBangLuong()
    elif ans == '7':
        print('---Chỉnh sửa nhân viên---')
        ChinhSuaNV()
    elif ans == '8':
        exit()
    else:
        print('Vui lòng chọn chức năng được liệt kê ở trên')
        main()
main()


