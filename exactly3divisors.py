# Exactly 3 Divisors 
# Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

# Input:
# The first line contains integer T, denoting number of test cases. Then T test cases follow. The only line of each test case contains an integer N.

# Output:
# For each testcase, in a new line, print the answer of each test case.

# Your Task:
# This is a function problem. You only need to complete the function exactly3Divisors() that takes N as parameter and returns count of numbers less than or equal to N with exactly 3 divisors.

# Constraints :
# 1 <= T <= 100
# 1 <= N <= 109

# Example:
# Input :
# 3
# 6
# 10
# 30
# Output :
# 1
# 2
# 3


def isPrime(N):
    if (N==1):
        return False
    for i in range(2,1+int(math.sqrt(N))):
        if N%i==0:
            return False
    return True
    
# function to check the numbers with exactly 3 divisors
def exactly3Divisors(N):
    N = int(math.sqrt(N))
    counter=0 #Initializing counter to zero
    for i in range(1,N+1): #Running a loop from 1 to N
    
        #  A number N only has 3 divisors if it is a perfect square and its square root is a prime number,
        #  and we know the number of perfect squares less than N which is sqrt(N),
        #  so just checking if i is prime or not
        if(isPrime(i)): 
            counter+=1
    return counter

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        print(exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends