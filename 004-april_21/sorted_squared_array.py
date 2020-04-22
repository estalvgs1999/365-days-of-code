# ---------------------------------------
#                  DAY 4
#        Facebook Interview Question
#
#          SORTED SQUARED ARRAY
#  You have a sorted array of integers.
#  Write a function that returns a sorted
#  arrays containing the squares of those
#  integers. 
#  
#  Input array length 1 < N < 1000
#  Element -1000 < a[i] < 1000
#
#  Input/Output array must be sorted
#  by: @estalvgs1999
# --------------------------------------

# Solution 1
# Complexity => O(nlogn)

def sorted_squared_array_1(a):
    # Constrains
    if len(a) < 1 or len(a) > 1000:
        return -1 # Invalid input

    for i in range(len(a)):
        a[i] = a[i]**2 
    a.sort() # O(nlogn)
    return a

# Solution 2
# Complexity => O(n)

def sorted_squared_array(a):

    n = len(a)

    # Constrains
    if n < 1 or n > 1000:
        return -1 # Invalid input

    a_out = [0]*n # initialize a list w/ array size

    lp = 0 #left ptr
    rp = n-1 # rigth ptr
    
    for i in range(n-1,-1,-1): #(init,stop,step)
        if abs(a[lp]) > abs(a[rp]):
            a_out[i] = a[lp]**2
            lp += 1
        else:
            a_out[i] = a[rp]**2
            rp -= 1
    return a_out




if __name__ == "__main__":
    
    import tests
    tests.test()
