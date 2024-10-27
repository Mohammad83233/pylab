1)        
number = int(input("Enter a number: "))
factorial = 1


if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is", factorial)



2)    

n_terms = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a, b = 0, 1


if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci series:", a)
else:
    print("Fibonacci series:", end=" ")
    for _ in range(n_terms):
        print(a, end=" ")
        a, b = b, a + b



3)

numbers = [1, 2, 3, 4, 5]  # Example list, you can modify this list as needed
total_sum = 0


for num in numbers:
    total_sum += num

print("The sum of all items in the list is:", total_sum)


4)
import math


def all_digits_even(number):
    for digit in str(number):
        if int(digit) % 2 != 0:
            return False
    return True


start = 1000
end = 9999
result = []


for i in range(start, end + 1):
    root = math.isqrt(i)  # Get the integer square root
    if root * root == i and all_digits_even(i):  # Check if i is a perfect square and has all even digits
        result.append(i)

print("Four-digit numbers with all even digits that are perfect squares:", result)


5)
n = int(input("Enter a number: "))


print(f"Multiplication Table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


6)
# Input: The upper limit N
N = int(input("Enter the value of N: "))

count = 0  # Counter to keep track of alternate primes

print("Alternate prime numbers up to", N, "are:")

# Loop through numbers up to N
for num in range(2, N + 1):
    # Check if num is prime
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    # If num is prime, and it's an alternate prime, print it
    if is_prime:
        if count % 2 == 0:  # Print every second prime
            print(num, end=" ")
        count += 1


7)

upper_limit = int(input("Enter the upper limit: "))
total_sum = 0


for num in range(1, upper_limit):
    if num % 6 == 0 and num % 4 != 0:
        total_sum += num

print("The sum of all integers below", upper_limit, "that are divisible by 6 but not by 4 is:", total_sum)


8)
# Input: Upper limit
upper_limit = int(input("Enter the upper limit: "))

print("Sum of digits (prime values only) for each number in the range:")

# Loop through each number in the range
for num in range(1, upper_limit + 1):
    # Calculate the sum of digits
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10  # Add the last digit
        temp //= 10  # Remove the last digit

    # Check if the digit sum is prime
    if digit_sum <= 1:
        continue  # 0 and 1 are not prime numbers

    is_prime = True
    for i in range(2, int(digit_sum**0.5) + 1):
        if digit_sum % i == 0:
            is_prime = False
            break

    # Print the sum if it is prime
    if is_prime:
        print(f"Number: {num}, Sum of Digits: {digit_sum}")

9)
# Input: A number from the user
number = input("Enter a number: ")

# Check if the number is palindromic
is_palindrome = True
length = len(number)

# Compare the digits
for i in range(length // 2):
    if number[i] != number[length - 1 - i]:
        is_palindrome = False
        break

# Output the result
if is_palindrome:
    print(f"{number} is a palindromic number.")
else:
    print(f"{number} is not a palindromic number.")


10)
# Input: A number from the user
number = int(input("Enter a number to find its factors: "))

# Initialize the factor to 1
factor = 1

print(f"Factors of {number} are:")

# Use a while loop to find factors
while factor <= number:
    if number % factor == 0:
        print(factor)
    factor += 1  # Move to the next potential factor

11)
# Input: A number from the user
number = int(input("Enter a number: "))

# Initialize variables
original_number = number
sum_of_powers = 0
num_digits = len(str(number))  # Calculate the number of digits

# Calculate the sum of the digits raised to the power of num_digits
while number > 0:
    digit = number % 10  # Extract the last digit
    sum_of_powers += digit ** num_digits  # Raise the digit to the power of num_digits and add to sum
    number //= 10  # Remove the last digit

# Check if the original number is equal to the sum of powers
if original_number == sum_of_powers:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")


12)
# Input: Number of steps for the pyramid
N = int(input("Enter the number of steps: "))

# Loop through each step
for i in range(1, N + 1):
    # Initialize a list to store the current row's values
    row = []
    for j in range(1, i + 1):
        # Calculate the value as j * i
        value = j * i
        row.append(str(value))  # Convert value to string for easy joining

    # Join the values with a space and print the row
    print(" ".join(row))


13)

# Number of rows for the upper part of the pattern
rows = 5

# Upper part of the pattern
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line

# Lower part of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line

