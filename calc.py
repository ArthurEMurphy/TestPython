#calc.py
#Extreme calculator
#Art

#menu
def menu():
    print("="*30)
    print("Extreme Calculator")
    print("by Art")
    print("="*30)
    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[q] Exit")

option = ''
while option !="q":
    menu()
    option = str(input('Please, select an option: '))
    #print('Your selected option is ' + option)

    num1 = float(input('Please, enter the first number: '))
    num2 = float(input('Please, enter the second number: '))

    #print(f"DEBUG: num1:{num1} num2:{num2}")
    result = 0
    if option=="1":
        result = num1+num2
        print(f"The result is: {result}")
    elif option=="2":
        result = num1-num2
        print(f"The result is: {result}")
    elif option=="3":
        result = num1*num2
        print(f"The result is: {result}")
    elif option==("4"):
        if num2 != 0:
            result = num1/num2
            print(f"The result is: {result}")
        else:
            print('Error: Cannot divide by zero')
    input('Press enter to continue...')

