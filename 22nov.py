#Given:
#numbers = [1,2,3,4,5,6,7,8,9,10]
#Perform the following operations:
#.Use map() to generate squares of all numbers.
#2.Use filter() to extract even numbers.
#3.Use reduce() to calculate the sum of all numbers.
#Display all results.
#Sample Output:
#Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Even Numbers: [2, 4, 6, 8, 10]
#Sum: 55
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9,10]
square= list(map(lambda x :x*x ,numbers))
even= list(filter(lambda x:x%2==0,numbers))
total=reduce(lambda a,b:a+b,numbers)
print("squares",square)
print("evenno",even)
print("totalsum",total)
