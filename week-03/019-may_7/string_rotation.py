# ---------------------------------------
#                  DAY 19
#         Coding Interview Question
#
#            STRING ROTATION
#  Assume you have a method isSubstring
#  which checks ifone word is a substring
#  of another. 
#  Given two strings, s1 and s2, write
#  code to check if s2 is a rotation of
#  s1 using only one call to isSubstring
#  (e.g., Uwaterbottleuis a rotation of uerbottlewat U).
#  
#  Question 1.9 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

# Complexity => O(n)
def is_rotation(s1,s2):
    n,m = len(s1),len(s2)

    if n == m and n > 0:
        s = s1+s1;
        return s2 in s
    return False

if __name__ == "__main__":
    print(is_rotation('waterbottle','erbottlewat'))
