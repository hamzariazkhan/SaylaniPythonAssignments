# Part -2 Python Basics (Conditional Statements)

# 5) A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
servic_year=int(input("ENTER YOUR SERVICES YEAR "))
salary=int(input("ENTER YOUR SALARY "))
if servic_year>5 and salary:
    bonus=0.05*salary
    print(f"Congratulation for serve : you awarded bonus { bonus} ")
else :
    print("THANKS FOR SERVING")
    
# 6) Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
Age=int(input("ENTER YOUR AGE  "))
if Age >17:
    
    print ("YES : YOU ARE ELIGIBLE")
else :
    print("NOPE YOU ARE NOT ELIGIBLE")

# 7) Write a program to check whether a number entered by user is even or odd.
Number=int(input("ENTER YOUR AGE  "))
if Number % 2==0:

    print ("YES : ITS EVEN NUMBER")
else :
    print("ITS ODD NUMBER")
    
# 8) Write a program to check whether a number is divisible by 7 or not. Show Answer
Number=int(input("ENTER YOUR AGE  "))
if Number % 7==0:

    print (f"YES : ITS DIVISIBLE BY : {Number}  ")
else :
    print(f"ITS NOT DIVISIBLE BY 7 :{ Number}")
    
# 9) Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
Number=int(input("ENTER YOUR AGE  "))
if Number %5 ==0:

    print ( "HELLO")
else :
    print("Bye")

# 10) Write a program to display the last digit of a number.
# Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
lenght=int(input("Enter the lenght"))
breadht=int(input("Enter the breadht"))
if lenght==breadht:
    print("ITS SQUARE")
else :
    print("ITS RECTANGLE")

# 11) Take two int values from user and print greatest among them.
Amount_1=int(input("Enter the Amount_1"))
Amount_2=int(input("Enter the Amount_2"))
if Amount_1>=Amount_2:
    print(f"AMOUNT 1 IS GREATEST {Amount_1}")
else :
    print(f"AMOUNT 2 IS GREATEST {Amount_2}")

# 12) A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity = int(input("Enter the quantity: "))
cost_per_unit = 100


total_cost = quantity * cost_per_unit


if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost -= discount


print(f"The total cost is: {total_cost}")

# 13) A school has following rules for grading system:
#     a. Below 25 - F
#     b. 25 to 45 - E
#     c. 45 to 50 - D
#     d. 50 to 60 - C
#     e. 60 to 80 - B
#     f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks=int(input("Enter the marks"))
if marks>80:
    print("YOUR GRADE IS A ")
elif marks>=60:
    print("YOUR GRADE IS B ")
elif marks>=50:
    print("YOUR GRADE IS C ")
elif marks>=45:
    print("YOUR GRADE IS D ")
elif marks>=25:
    print("YOUR GRADE IS E ")
elif marks<25:
    print("YOUR GRADE IS F ")    

# 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.
    # Take following input from user
    # Number of classes held
    # Number of classes attended.
    # And print
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

Total_Classes=int(input("Enter the total class"))
Classes_attend=int(input("Enter the class attend"))
percentage_of_class=(Classes_attend/Total_Classes)*100
print(percentage_of_class)
if percentage_of_class>=70:

   print("YOU ARE ALLOW")
else:
    print("YOU ARE NOT ALLOW")
   
# 15) Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
medical_cause=str(input("Enter yu are medical cause"))
if percentage_of_class!="YES":

   print("YOU ARE ALLOW")
else:
    print("YOU ARE NOT ALLOW")

# 16) Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 17) Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
    # if employee is female, then she will work only in urban areas.
    # if employee is a male and age is in between 20 to 40 then he may work in anywhere
    # if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
    # And any other input of age should print "ERROR"

age = int(input("Enter your age: "))
gender = input("Enter your gender (M or F): ").upper()
marital_status = input("Enter your marital status (Y or N): ").upper()


if gender == "F":
    place_of_service = "urban areas"
elif gender == "M":
    if 20 <= age <= 40:
        place_of_service = "anywhere"
    elif 40 < age <= 60:
        place_of_service = "urban areas"
    else:
        place_of_service = "ERROR"
else:
    place_of_service = "ERROR"

print(f"Place of service: {place_of_service}")

# 18) Take input of age of 3 people by user and determine oldest and youngest among them.
# Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
# uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750
units = int(input("Enter the number of units: "))
bill_amount = 0


if units <= 100:
    bill_amount = 0
elif units <= 300:
    bill_amount = (units - 100) * 5
else:
    bill_amount = (200 * 5) + ((units - 300) * 10)

print(f"The total bill amount is Rs. {bill_amount}")

 