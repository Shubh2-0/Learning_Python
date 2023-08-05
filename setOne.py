# # S1 D3 Assignment - Set 1

# ## Set 1

# 1. **Hello, World!**: Write a Python program that prints "Hello, World!" to the console.
#     - *Input*: None
#     - *Output*: "Hello, World!"
print("Hello, World!");


# 2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
#     - *Input*: None
#     - *Output*: "Type of variable1: <class 'int'>, value: 10..."
name = "Shubham";
print(name,type(name))

age = 23;
print(age,type(age))

salary = 70000.70;
print(salary,type(salary))

indian = True;
print(indian,type(indian))

my_list = [1, 2, 3, 4, 5]
print(my_list,type(my_list))

my_dict = {"name": "Aman", "age": 20, "city": "Indore"}
print(my_dict,type(my_dict))

my_set = {1, 2, 3, 4, 5}
print(my_set,type(my_set))





# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."
list =[1,2,32,5,51,78,7,8,9,10]
list.append(40)
list.remove(5)
list.sort();
print(list)


# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"
list = [10,20,30,40];
print(sum(list));
print(sum(list)/len(list));




# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"
str2 = "shubham";
print(str2[::-1]);



# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

input_string = "Hello"
num_vowels = count_vowels(input_string)
print(f"Number of vowels: {num_vowels}")


# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True


    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")



# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

input_number = 5
factorial_result = factorial(input_number)
print(f"Factorial of {input_number} is {factorial_result}.")


# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci_sequence(n):
    sequence = [0, 1]

    if n == 1:
        return [0]
    elif n == 2:
        return sequence

    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

input_n = 5
fibonacci_result = fibonacci_sequence(input_n)
print(fibonacci_result)



# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"  

squares_list = [i**2 for i in range(1, 11)]
print(squares_list)

