# LISTS
#. 1) Write a program that accepts a list from user and print the alternate element of list. 
list=[]
n=int(input("Enter the of list "))
for i in range(n):
    ele=int(input())
    list.append(ele)
print(f"The Accurate list is .. {list}") 
for i in range(n):
    if i % 2 == 0:
        print(f"The Alternative list is {list[i]}")

# 2) Write a program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method.
list=[]
n=int(input("Enter the size of list "))
for i in range(n):
    ele=int(input())
    list.append(ele)
print(f"The Accurate list is .. {list}") 

new_list=list[::-1]
print(new_list)
list=[]
n=int(input("Enter the size of list "))
for i in range(n):
    ele=int(input())
    list.append(ele)
print(f"The Accurate list is .. {list}") 
max=list[0]
for num in list:
    if num>list:
        max=num
        print(max)
    
# 3) Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard. 

list= []
num_count = int(input("How many numbers do you want to input? "))
for i in range(num_count):
    number = float(input(f"Enter number {i + 1}: ")) 
    list.append(number)
largest_number = list[0]  
for number in list:
    if number > largest_number:
        largest_number = number
print("The largest number in the list is:", largest_number)

#. 4) Write a program that rotates the element of a list so that the element at the first index moves
#to thesecond index, the element in the second index moves to the third index, etc.,
#and the element in the lastindex moves to the first index. 
def rotate_list(lst):
    if len(lst) == 0:
        return lst  
    last_element = lst[-1]
   
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    
    lst[0] = last_element
    return lst


user_input = input("Enter the elements of the list separated by spaces: ")
elements = user_input.split()
rotated_list = rotate_list(elements)
print("Rotated list:", rotated_list)

# 5) Write a program that input a string and ask user to delete a given word from a string. 
def remove_word_from_string(original_string, word_to_remove):
    words = original_string.split()
   
    filtered_words = [word for word in words if word != word_to_remove]
    return ' '.join(filtered_words)
original_string = input("Enter a string: ")
word_to_remove = input("Enter the word you want to delete: ")
modified_string = remove_word_from_string(original_string, word_to_remove)

print("Modified string:", modified_string)
filtered_words = [word for word in words if word.lower() != word_to_remove.lower()]

# 6) Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It
#should print the date in the form March 12, 2021. 
def convert_date_format(date_string):
    month, day, year = date_string.split('/')
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month_name = month_names[int(month) - 1]
    return f"{month_name} {int(day)}, {year}"
user_input = input("Enter a date in the format mm/dd/yyyy: ")
try:
    formatted_date = convert_date_format(user_input)
    print("Formatted date:", formatted_date)
except (ValueError, IndexError):
    print("Invalid date format. Please enter the date in mm/dd/yyyy format.")

# 7) Write a program with a function that accepts a string from keyboard and create a new string after
#converting character of each word capitalized. For instance, if the sentence is "stop and smell the roses."
#the output should be "Stop And Smell The Roses"
# def capitalize_words(input_string):
#     words = input_string.split()
#     capitalized_words = [word.capitalize() for word in words]
#     return ' '.join(capitalized_words)


# user_input = input("Enter a sentence: ")


# result = capitalize_words(user_input)


# print("Capitalized sentence:", result)
sen=str(input('ENTER THE SENTENCE ....'))
print(f"Orignal sentence is {sen}")
print(sen.title())

#. 8) Find the sum of each row of matrix of size m x n. For example for the following matrix output will be
def sum_of_rows(matrix):
    
    row_sums = [sum(row) for row in matrix]
    return row_sums

def main():
   
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))
    
  
    matrix = []
    
   
    print("Enter the elements of the matrix row by row:")
    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            print(f"Error: Row {i + 1} must have exactly {n} elements.")
            return
        matrix.append(row)
    
   
    row_sums = sum_of_rows(matrix)
    
    
    print("Sum of each row:")
    for i, row_sum in enumerate(row_sums):
        print(f"Row {i + 1}: {row_sum}")

#Write a program to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Get the dimensions of the matrices
    n = len(matrix1)        # Number of rows in matrix1
    m = len(matrix1[0])     # Number of columns in matrix1
    p = len(matrix2[0])     # Number of columns in matrix2
    
    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(p)] for _ in range(n)]
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result_matrix

def main():
    # Input the dimensions of the matrices
    n = int(input("Enter the number of rows for the first matrix (A): "))
    m = int(input("Enter the number of columns for the first matrix (A) / number of rows for the second matrix (B): "))
    p = int(input("Enter the number of columns for the second matrix (B): "))
    
    # Initialize the matrices
    matrix1 = []
    matrix2 = []
    
    # Input the first matrix (A)
    print("Enter the elements of the first matrix (A) row by row:")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != m:
            print(f"Error: Row {i + 1} must have exactly {m} elements.")
            return
        matrix1.append(row)
    
    # Input the second matrix (B)
    print("Enter the elements of the second matrix (B) row by row:")
    for i in range(m):  # Note: number of rows for B is equal to number of columns for A
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != p:
            print(f"Error: Row {i + 1} must have exactly {p} elements.")
            return
        matrix2.append(row)
    
    # Multiply the two matrices
    result_matrix = multiply_matrices(matrix1, matrix2)
    
    # Print the resulting matrix
    print("Resulting matrix after multiplication (A * B):")
    for row in result_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()