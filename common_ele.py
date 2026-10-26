n1 = int(input("Enter the number of elements in list1 : "))
n2 = int(input("Enter the number of elements in list2 : "))
i=1
j=1
list1=[]
list2 = []
while(i<=n1):
    number1 = int(input("Enter the numbers for list1 : "))
    list1.append(number1)
    i=i+1
while(j<=n2):
    number2 = int(input("Enter the numbers for list2 : "))
    list2.append(number2)
    j=j+1
set1 = set(list1)
set2 = set(list2)
print(list(set1.intersection(set2)))


