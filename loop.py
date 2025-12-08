#Count How Many Even and Odd Numbers Are in a List\

for num in range(1,50):
   if(num % 2 == 0):
         print(f"Even Number: {num}")
   else:
       print(f"odd Number : {num}")


#Print a Triangle Pattern (Pyramid)

n = 5   
for i in range(1, n + 1):
    print("*" * i)


# Ask user how many numbers they want to enter
count = int(input("How many numbers do you want to sum? "))

total = 0

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    total += num

print("The total sum is:", total)
