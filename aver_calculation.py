def average(numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    avg = sum/len(numbers)
    print(avg)
average([10,20,30,40])