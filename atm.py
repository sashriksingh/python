balance = 10000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
n = int(input("Choose any one : "))
if(n>=1 and n<=4):
    match n:
        case 1:
            print("Balance = ",balance)
        case 2:
            deposit = int(input("Enter the amount to be deposited :"))
            balance = balance + deposit
            print("Balance = ",balance)
        case 3:
            withdraw = int(input("Enter the amount to be withdrawn :"))
            if(withdraw < balance):
                balance = balance - withdraw
                print("Balance = ",balance)
            else:
                print("Insufficient Balance")
        case 4:
            print("Thank You for using our ATM")            
else:
    print("Invalid Choice")

