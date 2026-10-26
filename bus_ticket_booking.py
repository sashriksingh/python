seats = [1,2,3,4,5,6,7,8,9,10]
print("Enter 1 to Book Seats")
print("Enter 2 to Exit")
count = 0
while(count!=2):
    count = int(input("Enter a choice : "))
    if(count==1):
        print("Available Seats : \n",seats)
        s = int(input("Enter seat number : "))
        if(s in seats ):
            seats.remove(s)
            print("Seat Booked Successfully")
        else:
            print("Seat Already Booked")
    elif(count == 2):
        print("Exit")
        break
    else:
        print("Invalid Choice")
