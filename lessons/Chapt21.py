# List Comprehension - [expression for value in iterable if condition]

#############EXAMPLE 1##############
doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

print(doubles)
print(triples)
print(squares)
#############EXAMPLE 2##############
# fruits = ["apple","banana","orange","coconut"]
# fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit.upper() for fruit in ["apple","banana","orange","coconut"]]

print(fruits)
#############EXAMPLE 3##############
numbers = [1,-2,3,-4,5,-6,7,-8]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num%2==0]
odd_nums = [num for num in numbers if not num%2==0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)