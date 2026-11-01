# Ввод значения x (для сходимости ряда должно быть |x| < 1)
x = float(input("Введите значение x (|x| < 1): "))
eps = 0.0001

current_sum = 0.0
i = 1

# Вычисляем первый член ряда
previous_sum = (- (x ** i) * (i + 1)) / ((i + 2) * i)

# Цикл продолжается, пока текущий член ряда по модулю больше или равен eps
while abs(abs(current_sum) - abs(previous_sum)) >= eps:
    previous_sum = current_sum
    i += 1
    # Вычисляем следующий член ряда
    a = (- (x ** i) * (i + 1)) / ((i + 2) * i)
    current_sum = previous_sum + a
    

result = round(current_sum, 6)  # округляем результат до шести знаков после запятой
print(f"Результат вычисления суммы: {result}")
print(f"Количество учтенных членов ряда: {i}")
