import math

a = float(input("Enter  a: "))
b = float(input("Enter  b: "))
c = float(input("Enter  c: "))

d = b * b - 4 * a * c

if discriminant >= 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are:", root1, "and", root2)
else:
    print("No real roots")
