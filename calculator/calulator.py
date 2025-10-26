HISTORY_FILE = "history.txt"
def show_history():
    file = open(HISTORY_FILE,'r')
    lines = file.readlines()
    if(len(lines)==0):
        print("file is empty , No history found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE,'w')
    file.close()
    print("History cleared successfully")



def save_to_file(expression,result):
    file1 = open(HISTORY_FILE,'a')
    file1.write(f"{expression} = {result}\n")
    file1.close()

def calculate(expression):
    parts = expression.split()
    if len(parts) != 3:
        print( "Error: Invalid expression format. Use: operand1 operator operand2")
        return  
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Error: Unsupported operator. Use +, -, *, or /.")
        return
    if result.is_integer():
        result = int(result) 
    save_to_file(expression,result)

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Calculate")
        print("2. Show History")
        print("3. Clear History")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            expression = input("Enter expression (e.g., 2 + 3): ")
            calculate(expression)
        elif choice == '2':
            show_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.") 
main()      
    


