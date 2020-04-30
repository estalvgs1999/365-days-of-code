# ---------------------------------------
#                   DAY 12
#         Coding Interview Question
#
#                 IS UNIQUE
#  Given two strings, write a method to 
#  decide if one is a permutation of the 
#  other.
#
#  (!) Asumming that is an ASCII str
#
#  Question 1.2 | ctci 6th edition
#
#  by: @estalvgs1999
# ----------------------------------------

# The permutations are performed on a set S, 
# so that each permutation is the set S 
# accommodated in all the different possible ways.

# Complexity => O(nlog[n])

def check_permutation(string_1,string_2):

    if len(string_1) != len(string_2): return False

    # Sort the strings                                                                          
    return sorted(string_1) == sorted(string_2) # sorted() time complexity


# Solution without sort the strings
# Complexity => O(n)
def check_permutation_v2(string_1,string_2):

    if len(string_1) != len(string_2): return False

    letters = [0 for _ in range(128)]

    # We simply iterate through this code, counting how many times each character appears.
    for char in string_1:
        c = ord(char)
        letters[c] += 1

    # Then, afterwards, we compare the two arrays.
    for char in string_2:
        c = ord(char)
        if letters[c] == 0: 
            return False

    return True



if __name__ == "__main__":
    s = 'sabc'
    z = 'bacs'
    print(check_permutation(s,z))
    print(check_permutation_v2(s,z))