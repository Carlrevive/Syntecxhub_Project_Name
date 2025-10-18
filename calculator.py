class calculator():
    def add():
        if operator=="+":
            return print(f"= {round(float(number1+number2), 5)}")
       
    def subtract():
        if operator=="-":
           return print(f"= {round(float(number1-number2), 5)}")
        
    def multiply():
        if operator=="*":
           return print(f"= {round(float(number1*number2), 5)}")
        
    def divide():
     try:
        if operator=="/":
             print(f"= {round(number1/number2, 3)}")
     except:
        print("Zero Division Error")


      
while True:
  
    number1 = float(input("Enter first number: "))
    operator = input("Enter the operation sign (+,-,*,/): ") 
    if operator!="+" and operator!="-" and operator!="*" and operator!="/":
        print("Invalid Operation Sign")
    number2 = float(input("Enter second number: "))
    calculator.add()  
    calculator.subtract()
    calculator.multiply()
    calculator.divide()
    exit_continue=input("Press 'E' for exit or 'Enter key' to continue calculation: ")
    if exit_continue:
       break








