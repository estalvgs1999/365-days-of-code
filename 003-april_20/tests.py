# Function that runs tests to function
from max_sum_subarray import *
from termcolor import colored

test_arrays =[  ([-2, 2, 5, -11, 6],7),
                ([-2, -3, 4, -1, -2, 1, 5, -3],7),
                ([1, 3, 4, 2, 14, -2, 4], 26),
                ([1, 2, 3, -2, 5],9),
                ([-1,-2,-2,-1,-3],-1),
                ([-2,-3,4,-1,-2,1,5,-3,4],8),
                ([2,4,6,8],20),
                ([-2,3,-7,5,-9],5),
                ([3,-4,7,-9,8,7],15),
                ([3,-4,9,-8,8,7],16) ]

def test1():

    correct = 0
   
    print('\nMAXIMUM SUM SUBARRAY TESTING\n'+'-'*30)

    for test in test_arrays:
        if array_max_consecutive_sum(test[0]) == test[1]:
            print(colored('TEST ------------> OK','green'))
            correct += 1
        else:
            print(colored('TEST ------------> FAIL','red'))

    print('🆗',colored('{0}/{1} tests passed'.format(correct,len(test_arrays)),'green'))

def test2():
    
    correct = 0
   
    print('\nMAXIMUM SUM SUBARRAY TESTING\n'+'-'*30)

    for test in test_arrays:
        if array_max_consecutive_sum_brute_force(test[0]) == test[1]:
            print(colored('TEST ------------> OK','green'))
            correct += 1
        else:
            print(colored('TEST ------------> FAIL','red'))

    print('🆗',colored('{0}/{1} tests passed'.format(correct,len(test_arrays)),'green'))