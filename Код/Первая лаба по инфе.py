x = float(input("Введите x "))
y = float(input("Введите y "))
b = 1 + abs(y - x) + (y + x)**2 / 2 + abs((y - x)**3) / 3
print("Значение b =", "%.2f" % b)
