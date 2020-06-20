# Smallest divisible number 
# Given a number n the task is to complete the function which returns an integer denoting the smallest number evenly divisible by each number from 1 to n.

# Input:
# The first line of input contains an integer T denoting the no of test cases then T test cases follow. Each line contains an integer N.

# Output:
# For each test case output will be in new line denoting the smallest number evenly divisible by each number from 1 to n.

# Constraints:
# 1<=T<=50
# 1<=n<=25

# Example(To be used only for expected output):
# Input:
# 2
# 3 
# 6
# Output:
# 6
# 60

import math
def getSmallestDivNum(n):
    #RETURN ans
    ans = 1
    for i in range(1, n + 1):
        ans = int((ans * i)/math.gcd(ans, i))
    return ans 
        
       
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        print(getSmallestDivNum(n))
# } Driver Code Ends