# ---------------------------------------
#                  DAY 3
#        Amazon Interview Question
#
#          MAXIMUM SUM SUBARRAY
#  Given an array of integers, find the
#  maximum possible sum you can get from
#  one of its contiguos subarrays. 
#  The subarray from which this sum comes
#  must contain at lest 1 element. 
#
#  by: @estalvgs1999
# ---------------------------------------

import tests

# SOLUTION 1
# complexity => =O(n)
# Algorithmic Paradigm: Dynamic Programming
#
# Kanades algorithm provides a solution that 
# does not require considering all possible 
# subarrays, as well as being of linear complexity. 
# It is fast and does not require extra memory.

def array_max_consecutive_sum(array):
    
    max_sum = array[0]
    current_sum = max_sum

    for i in range(1,len(array)):
        current_sum = max(array[i]+current_sum,array[i])
        max_sum = max(max_sum,current_sum)
    
    return max_sum

# SOLUTION 2
# complexity => =O(n²)
# This solution uses two pointers and adds the possible 
# consecutive subarrays and compares each time against 
# the maximum total sum, the algorithm is slow and not efficient.

def array_max_consecutive_sum_brute_force(array):
    
    max_sum = array[0]
    
    for i in range(len(array)):
        current_sum = 0
        for j in range(i,len(array)):
            current_sum+=array[j]
            max_sum = max(current_sum,max_sum)

    return max_sum

if __name__ == "__main__":
    tests.test1()
    tests.test2()