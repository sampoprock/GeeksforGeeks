# Digits In Factorial 
# Given an integer N. The task is to find the number of digits that appear in its factorial, where factorial is defined as, factorial(n) = 1*2*3*4……..*N and factorial(0) = 1.

# Input:
# The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of one line. The first line of each test case consists of an integer N.

# Output:
# Corresponding to each test case, in a new line, print the number of digits that appear in its factorial.

# Your Task:
# This is a function problem. You only need to complete the function digitsInFactorial() that takes N as parameter and returns number of digits in factorial of N.

# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)

# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 104

# Example:
# Input:
# 2
# 5
# 120
# Output:
# 3
# 199


#User function Template for python3


##Complete this function
def digitsInFactorial(N):
    #Your code here
    
    if (N < 0): 
        return 0; 
  
    if (N <= 1): 
        return 1; 
  
    digits = 0; 
    for i in range(2, N + 1): 
        digits += math.log10(i); 
  
    return math.floor(digits) + 1; 


#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        
        print(digitsInFactorial(N))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends