import json

dep_dict = {}
with open('department_data.json') as dep_data:
    try:
        dep_dict = json.load(dep_data)
    except:
        pass
print(dep_dict)


department = input("Nhập mã bộ phận:")
if department not in dep_dict:
    print(f'Mã bộ phận chưa tồn tại, tạo mới ... {department}')
    while True:
        try:
            dep_bonus = int(input('Nhập thưởng bộ phận: '))
            dep_dict[department] = dep_bonus
            break
        except ValueError:
            print("Hãy nhập giá trị dưới dạng số")

dep_data = open('department_data.json','w')
json.dump(dep_dict,dep_data)
dep_data.close()