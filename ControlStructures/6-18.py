x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if x == 0 and y == 0:
    print(f"Point P({x},{y}) is the (0,0) point")
elif x == 0:
    print(f"Point P({x},{y}) is the y axis")
elif y == 0:
    print(f"Point P({x},{y}) is the x axis")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the 1st quadrant")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the 2nd quadrant")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the 3rd quadrant")
elif x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the 4th quadrant")
else:
    print("invaid coordinates")