# File thông tin thuế XML
info1 = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7"

#File Phạt muộn JSON
info2 =" https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de"

import urllib.request, urllib.parse, urllib.error
import json
import xml.etree.ElementTree as ET


file1 = urllib.request.urlopen(info1).read().decode()
data1 = ET.fromstring(file1)
tax_list = data1.findall('tax')
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
        self.gross_income = self.salary + self.bonus + self.bonus_salary
        self.taxable_income = self.gross_income * 0.895
        #Tính thuế
        file1 = urllib.request.urlopen(info1).read().decode()
        data1 = ET.fromstring(file1)
        tax_list = data1.findall('tax')
        for tax in tax_list:
            try:
                if int(tax.find('min').text) <= self.taxable_income/1000000 < int(tax.find('max').text):
                    self.tax_amount = int(tax.find('value').text)/100*self.taxable_income
                    
            except KeyError:
                if int(tax.find('min').text) <= self.taxable_income/1000000:
                    self.tax_amount = int(tax.find('value').text)/100*self.taxable_income

        self.net_income = self.taxable_income - self.tax_amount
        return self.net_income

    def tinhphat(self):
        file2 = urllib.request.urlopen(info2).read()
        data2 = json.loads(file2)
        for a in data2:
            try:
                if a['min'] <= self.late_comming_days <= a['max']:
                    return a['value']*self.late_comming_days
            except KeyError:
                return a['value']*self.late_comming_days

ab = Employee('NV01','Duong',200000,22,'MKT',1.2,1.1,2,200000)   
print(ab.tinhluong()) 