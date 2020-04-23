# -------------------------------------------
#                    DAY 6
#        Algorithm Optimization Question
#
#            0/1 KNAPSACK PROBLEM
#  Given a set of items, each with a weight
#  and a value, determine the number of each 
#  item to include in a collection so that 
#  the total weight is less than or equal 
#  to a given limit and the total value is 
#  as large as possible.
#
#  Suppose we have a knapsack which can hold
#  int w weight units. We have a total of n 
#  items to choose from, whose values are 
#  represented by an array int[] val and 
#  weights represented by an array int[] wt.
#  
#  Since this is the 0–1 knapsack problem, 
#  we can either include an item in our 
#  knapsack or exclude it, but not include 
#  a fraction of it, or include it multiple 
#  times.
#
#  by: @estalvgs1999
# -------------------------------------------

w = [1,2,4,2,5]
v = [5,3,5,3,2]

# Naive recursive solution
# Complexity: O(2^n)

def r_knapsack(n,C):
    N = n-1 #index
    if n == 0 or C == 0: return 0

    elif w[N] > C: return r_knapsack(n-1,C) # if item weight overpass the capacity, we don't take it.

    else:
        discard_item_val = r_knapsack(n-1,C) # ks value not taking the item
        taking_item_val = v[N] + r_knapsack(n-1,C - w[N]) # ks value taking the item
        return max(discard_item_val,taking_item_val) # we keep the item if it increment our value and decrease our weight



# Dynamic Recursive Programing solution
# Complexity: O(nC)

import numpy as np

m = []
def dr_knapsack(n,C):
    global m 
    m = np.zeros((n,C))
    return ks(n,C)

def ks(n,c):
    N,C = n-1,c-1 #index
    
    if m[N][C] != 0: return m[N][C] # Not calculate again

    if n == 0 or c == 0: return 0

    elif w[N] > c: result = ks(n-1,c) # if item weight overpass the capacity, we don't take it.

    else:
        discard_item_val = ks(n-1,c) # ks value not taking the item
        taking_item_val = v[N] + ks(n-1,c - w[N]) # ks value taking the item
        result = max(discard_item_val,taking_item_val) # we keep the item if it increment our value and decrease our weight
    
    m[N][C] = result # Store the result
    return result

if __name__ == "__main__":
    dr_knapsack(5,10)
    print(m)