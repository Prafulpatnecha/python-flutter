
# Simple Calculator

while True :
    num1 = float(input("Enter Any One Number A : "))
    num2 = float(input("Enter Any One Number B : "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("→→→Enter another number to return to the calculator.←←←")

    num3 = input("Enter 1 to 4 Any One Number Type : ")
    if num3 == "1" :
        print("Result:",num1 + num2)
    elif num3 == "2" :
        print("Result:",num1 - num2)
    elif num3 == "3" :
        print("Result:",num1 * num2)
    elif num3 == "4" :
        if num1==1 and num2==0:
            print("Try Again!")
        else:
            print("Result:",num1 / num2)
    else:
        break
