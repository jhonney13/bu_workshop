x = float(input("Enter x : "))
y = float(input("Enter y : "))

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else :
    print("Quadrant IV")

