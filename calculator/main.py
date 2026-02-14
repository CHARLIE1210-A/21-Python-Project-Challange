from decimal import Decimal, getcontext, InvalidOperation
import math
import os

# ================= CONFIGURATION =================
getcontext().prec = 28 #High precision for financial calculations
HISTORY_FILE = "calculation_history.txt"

# ================= GLOBAL STATE =================
memory = Decimal('0')
angle_mode = "DEG" # DEG or RAD

# ================= UTILITY FUNCTIONS =================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def decimal_input(prompt):
    while True:
        try:
            return Decimal(input(prompt))
        except InvalidOperation:
            print("Invalid input. Please enter a valaid number.")

def save_history(entry):
    with open(HISTORY_FILE, 'a') as f:
        f.write(entry + '\n')
        
def display_result(result):
    print(f"\nResult: {result}")
    save_history(str(result))
   
# ================= BASIC OPERATIONS ================= 
def add(x,y): return x+y;
def subtract(x,y): return x-y;
def multiply(x,y): return x*y;
def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x/y;


# ================= SCIENTIFIC OPERATIONS =================
def power(x,y): return x**y;
def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return Decimal(x.sqrt())

def factorial(x):
    if x % 1 != 0 or x < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")

def log_base10(x):
    if x <= 0:
        raise ValueError("Logarithm is only definded for positive numbers.")
    return Decimal(math.log10(x))

def natural_log(x):
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return Decimal(math.log(x))


# ================= TRIGONOMETRY =================    
def to_radians(angle):
    return math.radians(angle) if angle_mode == "DEG" else angle

def sin(x): return Decimal(math.sin(to_radians(float(x))));
def cos(x): return Decimal(math.cos(to_radians(float(x))));
def tan(x): return Decimal(math.tan(to_radians(float(x))));

# ================= MEMORY OPERATIONS =================
def memory_add(value):
    global memory 
    memory += value
    print(f"Memory updated: {memory}")
        
def memory_subtract(value):
    global memory
    memory -= value
    print(f"Memory updated: {memory}")
    
def memory_clear():
    global memory
    memory = Decimal('0')
    print("Memory cleared.")
    
def memory_recall():
    print(f"Memory recall: {memory}")
    return memory



# ================= MENU =================
def show_menu():
    print(""" 
          ================= SCIENTIFIC CALCULATOR =================
          Basic Operations:
            1  ➜  Addition
            2  ➜  Subtraction
            3  ➜  Multiplication
            4  ➜  Division
          
          Scientific Operations:
            5  ➜  Power
            6  ➜  Square Root
            7  ➜  Factorial
            8  ➜  Log10
            9  ➜  Natural Log
            
            Trigonometric Functions:
            10 ➜  Sine
            11 ➜  Cosine
            12 ➜  Tangent
            
            Memory Funcions:
            13 m+ ➜  Memory Add
            14 m- ➜  Memory Subtract
            15 mc ➜  Memory Clear
            16 mr ➜  Memory Recall
            
            Others:
            17 mode ➜  Toggle Angle Mode (DEG/RAD)
            18 Evaluate Expression ➜  Evaluate Mathematical Expression
            19 Evaluate History ➜  Show Calculation History
            
            q ➜  Quit
            
          """)
    
    # ================= MAIN LOOP =================
def main():
    global angle_mode
    while True:
        show_menu()
        choice = input("Select an operation (or 'q' to 'quit'): ")
        
        try:
            if choice == 'q':
                print("Exiting calculator. GoodBye !!")
                break
            elif choice in {'1', '2', '3','4', '5'}:
                x = decimal_input("Enter first number: ")
                y = decimal_input("Enter second number: ")
                
                operations = {
                    '1' : add,
                    '2' : subtract,
                    '3' : multiply,
                    '4' : divide,
                    '5' : power,
                }
                
                result = operations[choice](x,y)
                display_result(result)
                
            elif choice in {'6', '7', '8', '9', '10', '11', '12'}:
                x = decimal_input("Enter number: ")
                
                operations = {
                    '6': square_root,
                    '7': factorial,
                    '8': log_base10,
                    '9': natural_log,
                    '10': sin,
                    '11': cos,
                    '12': tan,
                }
            
                result = operations[choice](x)
                display_result(result)
                
            elif choice == "13":
                memory_add(decimal_input("Enter number to add to memory: "))
            elif choice == "14":
                memory_subtract(decimal_input("Enter number to subtract from memory: "))
                
            elif choice == "15":
                display_result(memory_recall())
                
            elif choice == "16":
                memory_clear()
                
            elif choice == "17":
                angle_mode = "RAD" if angle_mode == "DEG" else "DEG"
                print(f"Angle mode set to {angle_mode}")
                
            elif choice == "18":
                expr = input("Enter mathematical expression: ")
                result = Decimal(str(eval(expr)))
                display_result(result)
                
            elif choice == "19":
                print("\nCalculation History: ")
                if os.path.exists(HISTORY_FILE):
                    with open(HISTORY_FILE, 'r') as f:
                        print(f.read())
                        
                else:
                    print("No history found.")
                    
            
            else:
                print("Invalid choice.Please select a validoperation.")
                
        except Exception as e:
            print(f"Error: {e}")
                
                
if __name__ == "__main__":
    main()
                    
                    