# ---------------------------------------
#                   DAY 14
#         Coding Interview Question
#
#          PALINDROME PERMUTATION
#  Given a string, write a function to
#  check if it is a permutation of a
#  palindrome. 
#  A palindrome is a word or phrase that
#  is the same forwards and backwards. A
#  permutation is a rearrangement of
#  letters. The palindrome does not need
#  to be limited to just dictionary words
#  
#  >> Input: "Tact Coa"
#  >> Output: True (permutations:"taco cat'; "atco cta '; etc.)
#  
#  Question 1.4 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

# SOLUTION
# Complexity => O(n)
# 
# A palindrome is a string that is the same forwards and backwards. 
# Therefore, to decide if a string is a permutation of a palindrome,
# we need to know if it can be written such that it's the same 
# forwards and backwards.
# 
# What does it take to be able to write a set of characters the same
# way forwards and backwards? We need to have an even number of almost 
# all characters, so that half can be on one side and half can be on the other
# side. 
# At most one character (the middle character) can have an odd count

def is_palindrome_permutation(s):
    freq_table = char_count(s)
    return check_max_one_odd(freq_table)

# Count how many times each character appears
def char_count(input_string):

    char_table = {}

    for c in input_string:
        if c in char_table:
            char_table[c] += 1
        else:
            char_table[c] = 1

    return char_table

# Check that no more than one character has an odd count
def check_max_one_odd(freq_table):
    found_odd = False

    for x in freq_table.values():
        if x%2 != 0:
            if found_odd: return False
            found_odd = True
    return True



    