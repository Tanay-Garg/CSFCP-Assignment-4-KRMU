while True:
    print("CALCULATOR!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter the operation from above(1-5):"))

    if choice==5:
        break

    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))

    if choice==1:
        print("Result:",num1+num2)
    elif choice==2:
        print("Result:",num1-num2)
    elif choice==3:
        print("Result:",num1*num2)
    elif choice==4:
        print("Result:",num1/num2)
    else:
        print("Enter the correct choice(1-4)!!")