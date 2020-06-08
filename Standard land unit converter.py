print("\t\tArea Converter\t\t\nUse alphanumeric characters for input as shown in per question\n")
print("a = square-kilometer")
print("b = square-Meter")
print("c = square-Mile")
print("d = square-Foot")
print("e = square-Yard")
print("f = square-Inch")
print("g = Hectare")
print("h = Acre\n")

dict = {
    "a": "Square-kilometer",
    "b": "Square-Meter",
    "c": "Square-Mile",
    "d": "Square-Foot",
    "e": "Square-Yard",
    "f": "Square-Inch",
    "g": "Hectare",
    "h": "Acre"}
dict2 = {
    "a": "Square-km",
    "b": "Square-M",
    "c": "Square-Mile",
    "d": "Square-Ft",
    "e": "Square-Yard",
    "f": "Square-Inch",
    "g": "Hectare",
    "h": "Acre"}

inp3 = float(input("Enter Value: \n"))
inp = input("Enter the First Unit (As a ,b ,c,etc.): \n")
print("OK ,", inp3, dict[inp])
inp2 = input("Convert into: \n")

# For Square-Kilometer

if inp == "a" and inp2 == "a":
    print("None")
elif inp == "a" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 * 1000000, dict2[inp2])
elif inp == "a" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 2.59, dict2[inp2])
elif inp == "a" and inp2 == "d":
    print(inp3, dict2[inp], "=", inp3 * 10760000, dict2[inp2])
elif inp == "a" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 * 1196000, dict2[inp2])
elif inp == "a" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 1550000000, dict2[inp2])
elif inp == "a" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 * 100, dict2[inp2])
elif inp == "a" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 * 247, dict2[inp2])

# For Square-Meter

elif inp == "b" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 / 0.000001, dict2[inp2])
elif inp == "b" and inp2 == "b":
    print("None")
elif inp == "b" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 2590000, dict2[inp2])
elif inp == "b" and inp2 == "d":
    print(iinp3, dict2[inp], "=", np3 * 10.764, dict2[inp2])
elif inp == "b" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 * 1.196, dict2[inp2])
elif inp == "b" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 1550, dict2[inp2])
elif inp == "b" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 / 10000, dict2[inp2])
elif inp == "b" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 / 4047, dict2[inp2])

# For Square-Mile

elif inp == "c" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 * 2.59, dict2[inp2])
elif inp == "c" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 * 2590000, dict2[inp2])
elif inp == "c" and inp2 == "c":
    print("None")
elif inp == "c" and inp2 == "d":
    print(inp3, dict2[inp], "=", inp3 * 27880000, dict2[inp2])
elif inp == "c" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 * 3098000, dict2[inp2])
elif inp == "c" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 4014000000, dict2[inp2])
elif inp == "c" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 * 259, dict2[inp2])
elif inp == "c" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 * 640, dict2[inp2])

# For square-ft

elif inp == "d" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 / 43560, dict2[inp2])
elif inp == "d" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 / 10.764, dict2[inp2])
elif inp == "d" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 27880000, dict2[inp2])
elif inp == "d" and inp2 == "d":
    print("None")
elif inp == "d" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 / 9, dict2[inp2])
elif inp == "d" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 144, dict2[inp2])
elif inp == "d" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 / 107639, dict2[inp2])
elif inp == "d" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 / 43560, dict2[inp2])

# For square-yard

elif inp == "e" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 / 1196000, dict2[inp2])
elif inp == "e" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 / 1.196, dict2[inp2])
elif inp == "e" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 3098000, dict2[inp2])
elif inp == "e" and inp2 == "d":
    print(inp3, dict2[inp], "=", inp3 * 9, dict2[inp2])
elif inp == "e" and inp2 == "e":
    print("None")
elif inp == "e" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 1296, dict2[inp2])
elif inp == "e" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 / 11960, dict2[inp2])
elif inp == "e" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 / 4840, dict2[inp2])

# For square-inch

elif inp == "f" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 / 1550000000, dict2[inp2])
elif inp == "f" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 / 1550, dict2[inp2])
elif inp == "f" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 4014000000, dict2[inp2])
elif inp == "f" and inp2 == "d":
    print(inp3, dict2[inp], "=", inp3 * 144, dict2[inp2])
elif inp == "f" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 / 1296, dict2[inp2])
elif inp == "f" and inp2 == "f":
    print("None")
elif inp == "f" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 / 15500000, dict2[inp2])
elif inp == "f" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 / 6273000, dict2[inp2])

# For Hectare

elif inp == "g" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 / 100, dict2[inp2])
elif inp == "g" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 * 10000, dict2[inp2])
elif inp == "g" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 259, dict2[inp2])
elif inp == "g" and inp2 == "d":
    print(inp3, dict2[inp], "=", inp3 * 107639, dict2[inp2])
elif inp == "g" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 * 11960, dict2[inp2])
elif inp == "g" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 15500000, dict2[inp2])
elif inp == "g" and inp2 == "g":
    print("None")
elif inp == "g" and inp2 == "h":
    print(inp3, dict2[inp], "=", inp3 * 2.471, dict2[inp2])

# For Hectare

elif inp == "h" and inp2 == "a":
    print(inp3, dict2[inp], "=", inp3 / 247, dict2[inp2])
elif inp == "h" and inp2 == "b":
    print(inp3, dict2[inp], "=", inp3 * 4047, dict2[inp2])
elif inp == "h" and inp2 == "c":
    print(inp3, dict2[inp], "=", inp3 / 640, dict2[inp2])
elif inp == "h" and inp2 == "d":
    print(inp3, dict2[inp], "=", inp3 * 43560, dict2[inp2])
elif inp == "h" and inp2 == "e":
    print(inp3, dict2[inp], "=", inp3 * 4840, dict2[inp2])
elif inp == "h" and inp2 == "f":
    print(inp3, dict2[inp], "=", inp3 * 6273000, dict2[inp2])
elif inp == "h" and inp2 == "g":
    print(inp3, dict2[inp], "=", inp3 / 2.471, dict2[inp2])
elif inp == "h" and inp2 == "h":
    print("None")
else:
    print("Error!..Invalid input(Please check your input)")