balance = 10000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
n=0
while(n!=4):
    n = int(input("Enter your choice :"))
    if(n==1):
        print("Balance : ",balance)
    elif(n==2):
        deposit = int(input("Deposit Amount : "))
        balance = balance + deposit
        print("New Balance = ",balance)
    elif(n==3):
        withdraw = int(input("Withdrawal Amount : "))
        if(withdraw<balance):
            balance = balance - withdraw
            print("Balance = Rs",balance)
        else:
            print("Invalid")
    else: 
        print("Thank You for using our atm")
