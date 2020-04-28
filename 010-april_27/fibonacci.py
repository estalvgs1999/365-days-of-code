# ------------------------------------------
#                  DAY 10
#          Code Interview Question
#
#                FIBONACCI
#  Function for nth fibonacci number using 
#  Dynamic Programing.
#
#  { Fn = Fn-1 + Fn-2, F0 = 0 and F1 = 1
#  con n >= 0
#
#  by: @estalvgs1999
# ------------------------------------------


# Dynamic Programing
# Complexity => O(n)

fib_array = [0,1]
def fibonacci(n):

    if n <= 1: return fib_array[n] 
    elif n <= len(fib_array):
        return fib_array[n-1]
    
    temp_fib = fibonacci(n-1)+fibonacci(n-2)
    fib_array.append(temp_fib)
    return temp_fib


if __name__ == "__main__":
    
    print(fibonacci(9))
    print(fib_array)