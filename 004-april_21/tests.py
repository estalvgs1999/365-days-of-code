# Function that runs tests to function
from sorted_squared_array import *
from termcolor import colored

test_arrays =[  ([-6,-4,1,2,3,5],[1,4,9,16,25,36]),
                ([],-1),
                ([0]*1000,[0]*1000),
                ([]*2000,-1),
                ([-7,-3,-1,4,8,12],[1,9,16,49,64,144]),
                ([1,2,3],[1,4,9]),
                ([-3,-2,-1],[1,4,9])]


def test():
    
    correct = 0
   
    print('\nSORTED SQUARED ARRAY TESTING\n'+'-'*30)

    for test in test_arrays:
        ans = sorted_squared_array(test[0])
        if ans == test[1]:
            print(colored('TEST ------------> OK','green'))
            correct += 1
        else:
            print(colored('TEST ------------> FAIL','red'))
            print(colored('Test: {0}\nExpected Output {1} \nYour Output:{2}'.format(test[0],test[1],ans),'red'))

    print('🆗',colored('{0}/{1} tests passed'.format(correct,len(test_arrays)),'green'))