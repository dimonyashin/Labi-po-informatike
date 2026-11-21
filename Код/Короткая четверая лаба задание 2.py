def Udalenie(x, y):
    result = ""
    for letter in x:
        if letter not in y:
            result += letter
    return result

print(Udalenie("вечеринка", "елка"))