# GP Term 
# Given the first 2 terms A and B of a Geometric Series. The task is to find the Nth term of the series.

# Input:
# First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case in its first line contains two positive integer A and B (First 2 terms of GP). In the second line of every test case it contains of an integer N.

# Output:
# In each seperate line print the Nth term of the Geometric Progression. Print the floor ( floor(2.3)=2 ) of the answer.

# Your Task:
# This is a function problem. You need to complete the function termOfGP() that takes A and B as parameter and returns Nth term of GP. The return value should be double that would be automatically converted to floor by the driver code.

# Expected Time Complexity : O(logN)
# Expected Auxilliary Space : O(1)

# Constraints:
# 1 <= T <= 100
# -100 <= A <= 100
# -100 <= B <= 100
# 1 <= N <= 5

# Example:
# Input:
# 2
# 2 3
# 1
# 1 2
# 2
# Output:
# 2
# 2


#User function Template for python3

#Compelte his function
def termOfGP(A,B,N):
    #Your code here
    return math.floor((A* ((B/A)**(N-1))))



#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        
        print(math.floor(termOfGP(A,B,N)))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends