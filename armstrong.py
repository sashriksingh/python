n = int(input("Enter a Number : "))
number = n
sum = 0
while(n!=0):
    d = n%10
    n=int(n/10)
    sum = sum + (d**3)
print("Sum : ",sum)
if(sum == number):
    print("The Number is Armstrong")
else:
    print("The Number is Not Armstrong")
