def calculator(a,b,n):
    if(n==1):
        print("Sum : ",a+b)
    elif(n==2):
        print("Difference :",a-b)
    elif(n==3):
        print("Product : ",a*b)
    elif(n==4):
        print("Quotient : ",a/b)
    else:
        print("Invalid Choice")
number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divison")
choice = int(input("Enter a choice : "))
calculator(number1, number2, choice)
