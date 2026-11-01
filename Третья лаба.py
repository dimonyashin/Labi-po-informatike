A = -6.0          
B = 6.0                     
h = 1.0

print(f"{'Аргумент (x)'} | {'Функция F(x) = |x^3|'}")

x = A

while x <= B : 
    
    F_x = abs(x ** 3)
    
    print(f"{x}         | {F_x}")
    
    x += h