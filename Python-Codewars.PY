# Welcome. In this kata, you are asked to square every digit of a number
# For example, if we run 9119 through the function, 811181 will come
# out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns and integer
# 7kyu
# 8/3/2020

# def square_digits(num):
#   return int(''.join(str(int(i)**2)for i in str(num)))

# best practice

# def square_digits(num):
#   ret = ''
#   for x in str(num)
#     ret += str(int(x)**2)
#   return int(ret)

# Return the number (count) of vowels in the given string.
# We will consider AEIOU not Y as vowels
# Input string will only consist of lower case letters and/or spaces.

# def get_count(input_str):
#   num_vowels = 0
#   for i in input_str:
#     if i in "AEIOUaeiou":
#       num_vowels = num_vowels + 1
#   return num_vowels

# best practice

# def get_count(input_str):
#   return sum(1 for let in input_str if let in "aeiouAEIOU")

# Second best practice but I think is more readable

# def get_count(input_str):
#   return sum(i in 'aeiou' for i in input_str)

# Square(n)Sum
# Complete the square sum function so that it squared each number
# passed into it and then sums the results together.
# For example, for [1,2,2] it should return 9
# 8/6/2020
# 8kyu

# def square_sum(numbers):
#   total_sum = 0
#   for i in numbers:
#     total_sum = i * i + total_sum
#   return total_sum

# refactored/best practice

# def square_sum(numbers):
#   return sum(i ** 2 for i in numbers)

# Array.diff
# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b
# If a value is present in b, all of its occurences must be removed from the other

# def array_diff(a, b)
#   return [i for i in a if i not in b]

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
# 6kyu
# 8/20/2020

# def unique_in_order(iterable):
#   uniques = []
#   prev = None
#   for char in iterable:
#     if char != prev:
#       uniques.append(char)
#       prev = char

#   return uniques

# below is best practice

# def unique_in_order(iterable):
#   result = []
#   prev = None
#   for char in iterable[0:]:
#     if char != prev:
#       result.append(char)
#       prev = char
#   return result

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

# def nb_year(p0, percent, aug, p):
#   n = 0
#   while p0 < p:
#     n = n + 1
#     p0 = p0 + (p0 * percent/100) + aug

#     if p0 >= p:
#       return n

# best practice

# def nb_year(p0, percent, aug, p):
#   n = 0
#   while p0 < p:
#     p0 += p0 * percent / 100. + aug
#     n += 1
#   return n

# Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he
# does, he wants to know how many years 'Y' this sum 'P' has to be kept
# in the bank in order for it to amount to a desired sum of money 'D'.

# The sum is kept for 'Y' years in the bank where interest 'I' is paid
# yearly. After paying taxes 'T' for the year the new sum is re-invested.

# Note to Tax: not the invested principal is taxed, but only the year's
# accrued interest

# Example:

#   Let P be the Principal = 1000.00      
#   Let I be the Interest Rate = 0.05      
#   Let T be the Tax Rate = 0.18      
#   Let D be the Desired Sum = 1100.00


# After 1st Year -->
#   P = 1041.00
# After 2nd Year -->
#   P = 1083.86
# After 3rd Year -->
#   P = 1128.30
# Thus Mr. Scrooge has to wait for 3 years for the initial principal to
# amount to the desired sum.

# Your task is to complete the method provided and return the number of
# years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.

# Assumption: Assume that Desired Principal 'D' is always greater than
# the initial principal. However it is best to take into consideration
# that if Desired Principal 'D' is equal to Principal 'P' this should
# return 0 Years.
# 7kyu
# 8/25/2020
# Super similar to yesterday's Kata

# def calculate_years(principal, interest, tax, desired):
#     n = 0
    
#     if desired == principal:
#         n = 0
    
#     while principal < desired:
#         principal = principal + ((interest * principal) * (1 - tax))
#         n = n + 1
        
#     return n

# Best practice solution, again don't need the if statement I used in
# my solution, also += instead of reassigning value, pretty similar otherwise.

# def calculate_years(principal, interest, tax, desired):
#     years = 0
    
#     while principal < desired:
#         principal += (interest * principal) * (1 - tax)
#         years += 1
        
#     return years

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on
# their places.

# Zero isn't an odd number and you don't need to move it. If you have an
# empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
# 6kyu
# 8/26/2020
# Had to do some googling for this Kata

# First approach that did not work but was close

# def sort_array(source_array):
#   for i in range(0, len(source_array)):
#     for j in range(i, len(source_array)):
#       if(source_array[i] % 2 != 0 and source_array[j] % 2 != 0):
#         if(source_array[j] < source_array[i]):
#           aux = source_array[i]
#           source_array[i] = source_array[j]
#           source_array[j] = aux
#           return source_array

# After some googling and learning the sorted() method, messing with
# reverse and using .pop() made this much simpler but was definitely
# a challenge for sure

# def sort_array(source_array):
#   odds = sorted((i for i in source_array if i % 2 != 0), reverse = True)
#   return [i if i % 2 == 0 else odds.pop() for i in source_array]

# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as
# "C" and "G". You have function with one side of the DNA (string, except
# for Haskell); you need to get the other complementary side. DNA strand
# is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here
# http://rosalind.info/problems/list-view/ (source)

# DNA_strand ("ATTGC") return "TAACG"

# DNA_strand ("GTAT") return "CATA"
# 7kyu, 8/27/2020
# Went a totally different route at first then discovered translate!
# Python gets cooler to me everyday!

# def DNA_strand(dna):
#   return dna.translate(str.maketrans('AaTtCcGg', 'TtAaGgCc'))

# best practice, again I love Python bc it's pretty similar to my solution

# def DNA_strand(dna):
#   return dna.translate(string.maketrans("ATCG", "TAGC"))

# Write a function, persistence, that takes in a positive parameter num
# and returns its multiplicative persistence, which is the number of
# times you must multiply the digits in num until you reach a single
# digit.

# For example:

#  persistence(39) => 3  Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        and 4 has only one digit.

#  persistence(999) => 4 Because 9*9*9 = 729, 7*2*9 = 126,
#                        1*2*6 = 12, and finally 1*2 = 2.

#  persistence(4) => 0   Because 4 is already a one-digit number.
# 6kyu 8/31/2020
# I had no idea what a multiplicative persistence was, so I learned
# more than some code today. Inspired a blog post.

# def persistence(n):
#   multiplicative_persistence = 0
#   while n > 9:
#     multiplicative_persistence += 1
#     total = 1
#     n_as_string = str(n)
#     for i in n_as_string:
#       total = total * int(i)
#       n = total
#   return multiplicative_persistence

# best practice

# import operator
# def persistence(n):
#   i = 0
#   while n >= 10:
#     n = reduce(operator.mul, [int(x) for x in str(n)], 1)
#     i += 1
#   return i

# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples
# divisors(4)  = 3  // 1, 2, 4
# divisors(5)  = 2  // 1, 5
# divisors(12) = 6  // 1, 2, 3, 4, 6, 12
# divisors(30) = 8  // 1, 2, 3, 5, 6, 10, 15, 30
# 7kyu, completed in JS but originally solved it by completing it in
# Python
# 9/1/2020
# not sure why when I execute this code it does not return the correct
# answer?

# def divisors(n):
#     count = 0
#     div_by = 0
#     while n > div_by:
#         div_by += 1
#         if n % div_by == 0:
#             count += 1
#     return count

# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') returns true
# solution('abc', 'd') returns false
# I've seen an endswith() method before and worked very well here
# Simple as that!
# 7kyu
# 9/4/2020

# def solution(string, ending):
#     return string.endswith(ending)

# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels
# from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new
# string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become
# "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# def disemvowel(string):
#     vowels = 'aeiouAEIOU'
#     for vowel in vowels:
#         string = string.replace(vowel, '')
#     return string

# best practice

# def disemvowel(string):
#     return string.translate(None, 'aeiouAEIOU')

# Write an algorithm that will identify valid IPv4 addresses in
# dot-decimal format. IPs should be considered valid if they consist of
# four octets, with values between 0 and 255, inclusive.

# Input to the function is guaranteed to be a single string.

# Examples
# Valid inputs:

# 1.2.3.4
# 123.45.67.89
# Invalid inputs:

# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Note that leading zeros (e.g. 01.02.03.04) are considered invalid.
# 6kyu
# 9/11/2020

# def is_valid_IP(strng):
#     a = strng.split('.')
#     if len(a) != 4:
#         return False
#     for x in a:
#         if not x.isdigit():
#             return False
#         i = int(x)
#         if i > 0 and x.startswith('0'):
#             return False
#         if i < 0 or i > 255:
#             return False
#     return True

# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    n_as_string = []
    for x in n:
        n_as_string.append(''.join(str(x)))
    phone_number = "(" + "".join(n_as_string[0:3]) + " " + "".join(n_as_string[3:6] + "-" + "".join(n_as_string[6:10]))
    return phone_number