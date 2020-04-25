# ---------------------------------------
#                  DAY 7
#         Code Interview Question
#
#      LONGEST CONSECUTIVE CHARACTERS
#  Given a string, find the longest sub-
#  sequence consisting of a single cha-
#  racter.  
#  Example: 
#  >> longest("ABAACDDDBBA") 
#  >> should return {'D': 3}.
#
#  Input/Output array must be sorted
#  by: @estalvgs1999
# --------------------------------------

# SOLUTION
# Complexity => O(n)

def longest(s):

    current_count = 0
    max_count = 0
    max_char = None
    prev_char = None

    for current_char in s:

        if prev_char == current_char:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_count:
            max_count = current_count
            max_char = current_char
        
        prev_char = current_char

    return {max_char:max_count}


if __name__ == "__main__":
    print(longest('ABAACDDDBBA'))    