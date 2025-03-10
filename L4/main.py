# 2 conditions

# prefered_color = "Black"
# prefered_brand = "iPhone"

# 1
# CLI Command Line Interface
# GUI Graphical User Interface
color = input("Color: ")
brand = input("Brand: ")

print("Store has " + color + " " + brand)

if color == "Black" and (brand == "iPhone" or brand == "Samsung"):
    print("I am buying this phone!")
elif (color == "Pink" or color == "Purple") and brand == "Samsung":
    print("My sister is buying this phone!")
else:
    print("No one likes this phone!")



