import math

x1 = float(input("Введіть координату x1: "))
y1 = float(input("Введіть координату y1: "))
x2 = float(input("Введіть координату x2: "))
y2 = float(input("Введіть координату y2: "))
angle_OA = math.atan2(y1, x1)
angle_OB = math.atan2(y2, x2)
angle_OA = math.degrees(angle_OA)
angle_OB = math.degrees(angle_OB)
if angle_OA > angle_OB:
    print("Відрізок OA утворює більший кут з віссю OX")
else:
    print("Відрізок OB утворює більший кут з віссю OX")