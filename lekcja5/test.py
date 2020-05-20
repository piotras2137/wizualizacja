def fibonacchi(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)
print(fibonacchi(25))
def silnia(n):
    if(n==1):
        return 1
    else:
        return silnia(n-1)*n
print(silnia(10))