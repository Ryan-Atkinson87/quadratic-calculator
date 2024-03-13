import math

x = 0
y = 0
a = 3
b = -2
c = -5

top = (b * b) - (4 * a * c)

if top > 0:
    x1 = (-b + math.sqrt(top)) / (2 * a)
    x2 = (-b - math.sqrt(top)) / (2 * a)
    print("x1 = ", x1, "x2 = ", x2)


if top == 0:
    x = -b / (2 * a)
    print(x)


if top < 0:
    print("No real roots")
    exit()



