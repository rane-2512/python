#Q1. Function Scope and Built-in Functions (2 Marks)
#Write a function analyze_numbers() that accepts a list of numbers and displays:
#1.Maximum value
#2.Minimum value
#3.Sum of all values
#4.Average value
#Use Python built-in functions.
#Sample Input:
#[10, 20, 30, 40]
#Sample Output:
#Maximum = 40
#Minimum = 10
#Sum = 100
#Average = 25

def a(num):
    maximum=max(num)
    minimum=min(num)
    sumtotal=sum(num)
    average=sumtotal/len(num)
    print("maximum:",maximum)
    print("minimum:",minimum)
    print("total_sum:",sumtotal)
    print("average=",int(average) if average.is_integer() else average)
list=[10,20,30,40]
a(list)
