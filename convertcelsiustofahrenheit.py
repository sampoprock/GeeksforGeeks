# Convert Celsius To Fahrenheit 
# Given a temperature in celsius C. You need to convert the given temperature to Fahrenheit.

# Input:
# The first line of input contains T, denoting number of testcases. Each testcase contains single integer C denoting the temperature in celsius.

# Output:
# For each testcase, in a new line, output the temperature in fahrenheit.

# Your Task:
# This is a function problem. You only need to complete the function CtoF that takes C as parameter and returns temperature in fahrenheit( in double). The flooring and printing is automatically done by the driver code.

# Note : Complete the task in constant time and space complexity.

# Constraints:
# 1 <= T <= 100
# 1 <= C <= 104

# Example:
# Input:
# 2
# 32
# 50
# Output:
# 89
# 122


#User function Template for python3

##Complete this function
def cToF(C):
    #Your code here
    return ((C*1.8)+32)



#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        C=int(input())
        print(math.floor(cToF(C)))
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends