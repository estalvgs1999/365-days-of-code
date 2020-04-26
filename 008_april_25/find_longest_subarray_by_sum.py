# ---------------------------------------
#                  DAY 8 
#       Facebook Interview Question 
#
#      FIND LONGEST SUBARRAY BY SUM 
#  
# Given an array of integers and a value 
#  of sum s, return the longest subarray 
#  whose elements add up to s.
#
#  Input:
#  s : sum; 0 < s < 10⁹
#  arr: int array
#         |_ 1 < arr.length < 10⁵
#         |_ 0 < arr[i] < 10⁴
# 
#  Output:
#  An array that contains two elements that
#  represents the left and right bounds of
#  the subarray respectively (1-based).
#  If there no subarray, return [-1] 
#
#  by: @estalvgs1999 
# ----------------------------------------

# SOLUTION
# Complexity => O(n)

def find_longest_subarray_by_sum(s,arr):
    
    c_sum = 0
    r_ptr,l_ptr = 0,0
    result = [-1]

    while r_ptr < len(arr):
        
        c_sum += arr[r_ptr]
        
        while l_ptr < r_ptr and c_sum > s:
            c_sum -= arr[l_ptr]
            l_ptr += 1

        if c_sum == s and (len(result) == 1 or result[1]-result[0] < r_ptr - l_ptr):
            result = [l_ptr+1,r_ptr+1]

        r_ptr += 1

    return result
    

if __name__ == "__main__":
    
    print(find_longest_subarray_by_sum(12,[1,2,3,7,5])) # --> [2,4]
    print(find_longest_subarray_by_sum(15,[1,2,3,4,5,6,7,8,9,10])) # --> [1,5]
    print(find_longest_subarray_by_sum(15,[1,2,3,4,5,0,0,0,6,7,8,9,10])) # --> [1,8]
    print(find_longest_subarray_by_sum(0,[1,2,3,4,5,0,0,0,6,7,8,9,10])) # --> [6,8]
    print(find_longest_subarray_by_sum(102,[1,2,3,4,5,6,7,8,9,10])) # --> [-1]