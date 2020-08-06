# Welcome. In this kata, you are asked to square every digit of a number
# For example, if we run 9119 through the function, 811181 will come
# out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns and integer
# 7kyu
# 8/3/2020

def square_digits(num):
  return int(''.join(str(int(i)**2)for i in str(num)))

# best practice

def square_digits(num):
  ret = ''
  for x in str(num)
    ret += str(int(x)**2)
  return int(ret)

# Return the number (count) of vowels in the given string.
# We will consider AEIOU not Y as vowels
# Input string will only consist of lower case letters and/or spaces.

def get_count(input_str):
  num_vowels = 0
  for i in input_str:
    if i in "AEIOUaeiou":
      num_vowels = num_vowels + 1
  return num_vowels

# best practice

def get_count(input_str):
  return sum(1 for let in input_str if let in "aeiouAEIOU")

# Second best practice but I think is more readable

def get_count(input_str):
  return sum(i in 'aeiou' for i in input_str)

# Square(n)Sum
# Complete the square sum function so that it squared each number
# passed into it and then sums the results together.
# For example, for [1,2,2] it should return 9
# 8/6/2020
# 8kyu

def square_sum(numbers):
  total_sum = 0
  for i in numbers:
    total_sum = i * i + total_sum
  return total_sum

# refactored/best practice

def square_sum(numbers):
  return sum(i ** 2 for i in numbers)

# Array.diff
# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b
# If a value is present in b, all of its occurences must be removed from the other

def array_diff(a, b)
  return [i for i in a if i not in b]