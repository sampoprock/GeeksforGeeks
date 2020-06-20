# Absolute Value 
# You are given an interger I. You need to print the absolute value of the interger I.

# Input:
# The first line of input contains T, denoting number of testcases. Each testcase contains single integer I which may be positive or negative.

# Output:
# For each testcase, in a new line, output the absolute value.

# Your Task:
# This is function problem. You only need to complete the function absolute that takes integer I as parameter and returns the absolute value of I. All other things are taken care of by the driver code.

# Expected Time and Space Complexity : O(1)

# Constraints:
# 1 <= T <= 100
# -106 <= I <= 106

# Example:
# Input:
# 2
# -32
# 45
# Output:
# 32
# 45


# User function Template for python3

# Complete this function


def absolute(I):
    # Your code here
    return abs(I)



#{ 
#Driver Code Starts.


def main():

    T = int(input()) #Input the number of testcases

    while(T > 0):
        I = int(input()) #input number
        print(absolute(I)) #Call function and print
        T -= 1 #Reduce number of testcases


if __name__ == "__main__":
    main()

#} Driver Code Ends