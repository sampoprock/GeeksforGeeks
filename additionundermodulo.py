# You are given two numbers a and b. You need to find the sum of a and b under modulo M.
# Note: Take M as 109+7

# Input:
# The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing a and b.

# Output:
# For each testcase, in a new line, print sum of a and b under modulo M.

# Your Task:
# This is a function problem. You need to complete the function sumUnderModulo that takes a and b as parameters and returns sum of a and b under modulo M.

# Note : Solve the problem in Constant time and space ccomplexity.

# Constraints:
# 1 <= T <= 105
# 1 <= a,b <= 263-1

# Examples:
# Input:
# 2
# 9223372036854775807 9223372036854775807
# 1000000007 1000000007
# Output:
# 582344006
# 0

def sumUnderModulo(a,b):
    '''
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    '''
    M = 1000000007
    # code here
    return ((a+b)%M)



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        print(sumUnderModulo(a,b))

# } Driver Code Ends