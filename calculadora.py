def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
def menu():
    print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")

while True:
    menu()
    choice = input("Enter choice(1/2/3/4/5): ")

    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
            print("Respuesta=", add(num1, num2))

    elif choice == '2':
            print("Respuesta=", subtract(num1, num2))

    elif choice == '3':
            print("Respuesta=", multiply(num1, num2))

    elif choice == '4':
            print("Respuesta=", divide(num1, num2))
        
    elif choice == '5':
            print("Exit")
            break
    else:
            print("Invalid Input")
