# ---------------------------------------
#                  DAY 16
#         Coding Interview Question
#
#            STRING COMPRESSION
#  Implement a method to perform basic
#  string compression using the counts
#  of repeated characters. For example,
#  the string aabcccccaaa would become
#  a2b1c5a3 . If the "compressed" string
#  would not become smaller than the
#  original string, your method should
#  return the original string.
#  
#  You can assume the string has only
#  uppercase and lowercase letters (a/z).
#  
#  Question 1.6 | ctci 6th edition
#
#  by: @estalvgs1999
# ---------------------------------------

# SOLUTION 1
# Complexity => O(p +k²)
# p: size of the original string; k: number of char sequences
# It's slow because string concatenation operates in O(n²)

def string_compression_v1(string):
    n = len(string)
    compressed_string = ""
    consecutive_count = 0

    for i in range(n):
        consecutive_count+=1
        if i+1 >= n or string[i] != string[i+1]:
            compressed_string += "{0}{1}".format(string[i],consecutive_count)
            consecutive_count = 0

    return compressed_string if n > len(compressed_string) else string


# SOLUTION 2
# Complexity => O(n+k) => O(N); N=n+k
# n: size of the original string; k: number of char sequences
# It's better than solution 1 because string join operates in O(n)

def string_compression_v2(string):
    n = len(string)
    compressed_string = ""
    consecutive_count = 0

    for i in range(n):
        consecutive_count+=1
        if i+1 >= n or string[i] != string[i+1]:
            compressed_string = ''.join([compressed_string,string[i],str(consecutive_count)])
            consecutive_count = 0

    return compressed_string if n > len(compressed_string) else string


# SOLUTION 3
# Complexity => O(n+k) => O(N); N= 2n+k
# n: size of the original string; k: number of char sequences; 
# This approach avoids compressing the string if its size is greater when compressing it.

def string_compression(string):
    
    n = len(string)
    if n < count_compression(string): # Avoid to do the entire algorithm
        return string

    compressed_string = ""
    consecutive_count = 0

    for i in range(n):
        consecutive_count+=1
        if i+1 >= n or string[i] != string[i+1]:
            compressed_string = ''.join([compressed_string,string[i],str(consecutive_count)])
            consecutive_count = 0

    return compressed_string

# Returns the length of the compressed string
# TC = O(n)
def count_compression(string):
    n = len(string)
    compressed_len = 0

    for i in range(n):
        if i+1 >= n or string[i] != string[i+1]:
            compressed_len += 2 # xn -> x: char/n: number of consecutive chars
    return compressed_len




if __name__ == "__main__":
    print(string_compression_v1('aabcccccaaa'))
    print(string_compression_v2('aabcccccaaa'))
    print(string_compression('aabcccccaaa'))