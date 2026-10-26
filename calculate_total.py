prices = [120, 250, 80, 150, 300]
sum=0
for i in range(5):
    sum = sum+prices[i]
print("Total Price = ",sum)
if(sum>=1000):
    print("You get a Discount")
else:
    print("No Discount")