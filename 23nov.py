#Q6. Decorator Implementation (3 Marks)
#Create a decorator named execution_time() that:
#Displays a message before function execution.
#Executes the function.
#Displays a message after function execution.
#Apply this decorator to a function that calculates the factorial of a number
def et(func): #Create a decorator named execution_time() that:
    def wrapper():
        print("function started")
        func()
        print("function finish")
    return wrapper
@et #Apply this decorator to a function
def factorial():
    num=5
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("factorial:",fact)
    
factorial()
