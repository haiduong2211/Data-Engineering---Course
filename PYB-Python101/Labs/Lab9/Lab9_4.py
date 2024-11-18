a = int(input())
b = int(input())
c = int(input())

if a == b and a ==c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
