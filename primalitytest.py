# Primality Test 
# For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

# Input:
# First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case should contain a positive integer N.

# Output:
# For each testcase, in a new line, print "Yes" if it is a prime number else print "No".

# Your Task:
# This is a function problem. You just need to complete the function isPrime that takes N as parameter and returns True if N is prime else returns false. The printing is done automatically by the driver code.

# Expected Time Complexity : O(N1/2)
# Expected Auxilliary Space :  O(1)

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 109

# Example:
# Input:
# 2
# 5
# 4
# Output:
# Yes
# No

#User function Template for python3


##Complete this function
def isPrime(N):
    #Your code here
    if(N<2):
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if(N%i==0):
            return False
            
    return True


#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        if(isPrime(N)):
            print("Yes")
        else:
            print("No")
            
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends