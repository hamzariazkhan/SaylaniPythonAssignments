# Looping Structures
# 1) Write a Python program to print the numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# 2) Write a Python program to print the numbers from 20 to 1 using a while loop
for i in range(20,0,-1):
    print(i)

# 3) Write a program to print even numbers from 1 to 10.
for i in range(1,11):
    if i%2==0:
        print(i)

# 4) Write a program that prompts the user to enter a number n and prints all the numbers from 1 to n.
n=int(input("ENTER THE NUM"))
for i in range(1,n+1):
    print(i)

# 5) Write a program that prompts the user to enter a number n, and then prints all the odd numbers between 1 and n.
n=int(input("ENTER THE NUM"))
for i in range(1,n+1):
    if i%2==1:
        print(i)

# 6) write a program that prints 'Happy Birthday!' five times on screen. 
for i in range(1,6):
    print("Happy Birthday!")

# 7) Write a program that takes a number n as input from the user and generates the first n terms of the series formed by squaring the natural numbers.
n=int(input("ENTER THE NUM"))
for i in range(1,n+1):
    print(i*i)

# 8) Write a program that prompts the user to input a number and prints its multiplication table.
n=int(input("ENTER THE NUM"))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

# 9) Write a Python program to print the first 8 terms of an arithmetic progression starting with 3 and having a common difference of 4.
first_term = 3
common_difference = 4
num_terms = 8
for i in range(num_terms):
    term = first_term + i * common_difference
    print(term, end=' ')
 
# 10) Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3. 
first_term = 2
common_ratio = 3
num_terms = 6
for i in range(num_terms):
    term = first_term * (common_ratio **i)
    print(term, end=' ')
 
import math
n=int(input())
total=0

for i in range(1,n+1):
    total+=i
    print(i)
    print(total)
    
list=[]
n=int(input("Enter the size  "))
new_ele=int((input()))
for i in range(0,n):
    
    new_ele=list.append(new_ele)
    print(new_ele)
# 11) Write a program that asks the user for a positive integer value. The program should calculate the sum of all the integers from 1 up to the number entered. For example, if the user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20. 
n=int(input("Enter the num "))
total=0
for i in range(1,n+1):
    total+=i
    print(i)
print(f"Total sum of give num is {total}")    
    
# 12) write a program that takes a positive integer N as input and calculates the sum of
#the reciprocals of all numbers from 1 up to N. The program should display the final sum. 
n=int(input("Enter the positive integer "))
total=0.0
for i in range(1,n+1):
    if n>0:
        total+=1/i
       
print(f"Total sum of give num is {total}")    
    
# 13) Write a program that prompts the user to enter a number and repeats this process 5 times. The program should accumulate the numbers entered and then display the finalrunning total. 
total=0
for i in range(5):
    n=int(input("ENTER THE NUM "))
    total+=n
    
    
print(f"Total sum of give num is {total}")
fac=1
n=int(input("ENTER THE fac NUM "))
for i in range(1,n+1):
    if n>0:
        
       fac=fac*i
    elif n<0:
        print("negative num have no fac")

print(f"The factorial of {n} is {fac} ")    
   
base=int(input("ENTER THE base  "))
power=int(input("ENTER THE power "))
# cal=base**power
# print(cal)
def c_power(base,power):
    result=1
    neg_exp=power<0
    power=abs(power)
    for i in range(power):
        result*=base
    if  neg_exp:
        result=1/result
    return result    
ans=c_power(base,power)
print(f"{base} is power is {power} so the anser is {ans}")

 