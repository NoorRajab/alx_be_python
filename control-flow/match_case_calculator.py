num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
    case "+":
        result = num1 + num2
        print(f"Result is {result}")
    case "-":
        result = num1 - num2
        print(f"Result is {result}")
    case "*":
        result = num1 * num2
        print(f"Result is {result}")
    case "/":
        if num2 == 0 :
            print("Zero may cause a problem during operation.")
        else:
            result = num1 / num2
            print(f"Result is {result}")
    case _:
        print("Sorry, this operation is not recognized")     
        
    
