def add():
    if operand=="+":
        return print(number1+number2)
   
def subtract():
    if operand=="-":
       return print(number1-number2)
    
def multiply():
    if operand=="*":
       return print(number1*number2)
    
def divide():
 try:
    if operand=="/":
         print(number1/number2)
 except:
    print("Zero Division Error")

def clear():
   if clear:
      clear
      
while True:
  
    number1 = int(input("Enter first number: "))
    operand = input("Enter the operation sign (+,-,*,/): ")  
    number2 = int(input("Enter second number: "))
    add()  
    subtract()
    multiply()
    divide()
    exit_continue=input("Press 'e' for exit or Enter key to continue calculation: ")
    if exit_continue:
       break





