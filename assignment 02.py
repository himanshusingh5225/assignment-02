# Task 1: Check if a Number is Even or Odd
n1=int(input("enter a number:"))
if n1%2==0 :
    print(n1, "is even number.")
else:
    print(n1," is odd number.")


#Task 2: Sum of Integers from 1 to 50 Using a Loop

#Initialize the sum variable
total_sum=0
# Use a loop to iterate through numbers 1 to 50
for i in range (1,51):
    total_sum+=i

print("sum of the numbers from 1 to 50 is:",total_sum)