import math

run = True

x = 0
y = 0




while run == True:
    print("\n")
    a_in = input("a =: ")
    b_in = input("b =: ")
    c_in = input("c =: ")

    a = float(a_in)
    b = float(b_in)
    c = float(c_in)

    top = (b * b) - (4 * a * c)
    axsym = -(b / (2 * a))
    y = (a*(axsym**2)) + (b * axsym) + c

    print("Axis of Symmetry = ", axsym)
    print("Vertex = (",axsym,", ",y,")")
    print("Discriminant = ", top)

    if top > 0:
        x1 = (-b + math.sqrt(top)) / (2 * a)
        x2 = (-b - math.sqrt(top)) / (2 * a)
        print("x1 = ", x1, "\nx2 = ", x2)

    if top == 0:
        x = -b / (2 * a)
        print("Parabola touches x axis at ", int(x))


    if top < 0:
        print("No real roots, cannot solve")
    
    again = input("Would you like to run another calculation? (y/n): ")
    if again == "n" or again == "N":
        run = False


