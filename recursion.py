#factorial 
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

    
factorial(4)
24
_________________________________________________________________________________________________________________
#fibonacci series

def fibonacci(n):
    if n ==0 :
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) +fibonacci(n-2)

    
fibonacci(3)
2
__________________________________________________________________________________________________________________
