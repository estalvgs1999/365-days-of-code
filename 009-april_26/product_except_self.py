# ---------------------------------------
#                   DAY 9
#         Apple Interview Question
#
#            PRODUCT EXCEPT SELF
#  Given an array nums of n integers where
#  n > 1, return an array such that out[i]
#  is equal to the product of all elements
#  except nums[i].
#
#  by: @estalvgs1999
# ----------------------------------------

# Brute Force Solution
# Complexity O(n²)
def bf_product_except_self(nums):

    output = []

    for i in range(len(nums)):
        current_product = 1
        for j in range(len(nums)):
            if i != j:   
                current_product *= nums[j]
        output.insert(i,current_product)

    return output

# Using division Solution 
# Complexity O(2n)
def ud_product_except_self(nums):

    p = 1
    for n in nums: p*=n
    output = [p//n for n in nums]
    
    return output

# Solution without division
# Complexity O(2n)
def product_except_self(nums):

    n = len(nums)
    output = [1]*n

    for i in range(1,n):
        output[i] = nums[i-1]*output[i-1]

    R = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i]*R
        R = R*nums[i]

    return output



if __name__ == "__main__":
    print(bf_product_except_self([1,2,3,4]))
    print(ud_product_except_self([1,2,3,4]))
    print(product_except_self([1,2,3,4]))