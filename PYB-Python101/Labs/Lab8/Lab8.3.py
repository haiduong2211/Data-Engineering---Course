s = input("Nhập dãy số cho trước: ").split()
c = [int(x) for x in s]
s = set(c)

a = input("Nhập số remove: ").split()
numbers_remove = [int(s) for s in a if s.isdigit()]

for num in numbers_remove:
    if num in s:
        s.remove(num)
        
print(sum(s))
