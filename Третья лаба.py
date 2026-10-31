A = -5.0          
B = 5.0                     
h = 1.0

print(f"{'Аргумент (x)'} | {'Функция F(x) = x^2'}")

x = A

while x <= B + h/2: 
    
    F_x = x ** 2
    
    print(f"{x} | {F_x}")
    
    x += h