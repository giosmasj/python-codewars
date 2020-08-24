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

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
# 6kyu
# 8/20/2020

def unique_in_order(iterable):
  uniques = []
  prev = None
  for char in iterable:
    if char != prev:
      uniques.append(char)
      prev = char

  return uniques

# below is best practice

def unique_in_order(iterable):
  result = []
  prev = None
  for char in iterable[0:]:
    if char != prev:
      result.append(char)
      prev = char
  return result

# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover
# 50 new inhabitants per year come to live in the town. How many years 
# does the town need to see its population greater or equal to p = 1200
# inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is
# an integer)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.
# More generally given parameters:

# p0, percent, aug (inhabitants coming or leaving each year), p
# (population to surpass)

# the function nb_year should return n number of entire years needed to
# get a population greater or equal to p.

# aug is an integer, percent a positive or null number, p0 and p are
# positive integers (> 0)

# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note: Don't forget to convert the percent parameter as a percentage in
# the body of your function: if the parameter percent is 2 you have to
# convert it to 0.02.
# 7ku
# 8/24/2020

def nb_year(p0, percent, aug, p):
  n = 0
  while p0 < p:
    n = n + 1
    p0 = p0 + (p0 * percent/100) + aug

    if p0 >= p:
      return n

# best practice

def nb_year(p0, percent, aug, p):
  n = 0
  while p0 < p:
    p0 += p0 * percent / 100. + aug
    n += 1
  return n