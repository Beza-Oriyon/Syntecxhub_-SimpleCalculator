def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0: 
        return "Error: Cannot divide y zero"
    
    return a/b

def main():

    while True:
     print("\n --- Simple Calculator ---")
     print("Select operation:")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")
     print("5. Exit")

     choice = input("Enter your choice (1-5): ")

     if choice == '5':
         print("Existing Calculator. See you next time")
         break
     
     if choice in ['1', '2', '3', '4']:
         
         num1= float(input("Enter first number:"))
         num2= float(input("Enter second number: "))

         if choice == "1":
             print("Result: ", add(num1, num2))
         elif choice == "2":
             print("Result: ", subtract(num1, num2)) 
         elif choice == "3":
             print("Result: ", multiply(num1, num2))
         elif choice == "4":
             print("Result: ", divide(num1, num2))
         else:
             print("Invalid input. Please select a valid operation.")


if __name__ == "__main__":
        main()  

   
'''We also can use match case statement instead of if-elif-else to make the code cleaner and more readable. Here's how to do it:
match choice: 
    case '1':
        print("Result: ", add(num1, num2))
    case '2':
        print("Result: ", subtract(num1, num2)) 
    case '3':
        print("Result: ", multiply(num1, num2))
    case '4':
        print("Result: ", divide(num1, num2))
    case _:
        print("Invalid input. Please select a valid operation.")  ''' 
