cases = {}
print("1. Add Case")
print("2. Search Case")
print("3. View Suspects")
print("4. Search Suspect")
print("5. Update Case Status")
print("6. Exit")
choice = 0
while(choice!=6):
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        casenumber = int(input("Case Number : "))
        title = input("Case Title : ")
        suspect = input("Enter the suspect : ")
        detective = input("Lead Detective : ")
        status = input("Case Status : ")

        cases[casenumber] = [title,suspect,detective,status]
        print(cases[casenumber])
    if choice == 2:
        cn = int(input("Enter the Case Number : "))
        if cn in cases:
            print(cases[cn])
        else:
            print("Case Not Found")
    if(choice == 3) : 
        for case in cases : 
         print(cases[case][1])
    if(choice == 4):   
        sus = input("Enter the Suspect Name : ")
        found = False
        for case in cases:
            if cases[case][1] == sus:
                print("Suspect Found")
                print("Case Number : ",case)
                found = True
        if found == False:
            print("Suspect Not Found")
    if(choice == 5):
        caseno = int(input("Enter the Case Number : "))
        if caseno in cases:
            st = input("Enter the Status of the case : ")
            cases[caseno][3]=st
            print("Case Status : ",cases[caseno][3])
    if(choice == 6):
        print("EXIT")
        break

