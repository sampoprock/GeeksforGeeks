# Quadratic Equation Roots 
# Given a quadratic equation in the form ax2 + bx + c. You need to print roots of it.

# Input:
# First line of input contains an integer, the number of test cases T. Each test case contains three positive numbers a, b and c in the same line seperated by space.

# Output: 
# If roots of equations exits, then print the two roots separated by space (Higher valued root should be printed before lower valued). If roots are imaginary, then print "Imaginary".

# Note 1 :  Please do NOT to add "\n" or newline after printing output in your function.  Newline is added by the driver code.
# Note 2 : Please do float division like (-b+sqrt(b2-4ac)) / 2.0*a.
# Note 3 : Please use floor function, note that roots can be negative.

# Your Task:
# This is a function problem. You only need to complete the function quadraticRoots that takes a,b,c as parameters and prints the floor value of roots. The other tasks are already performed by the driver function. The newline is already appended by the driver code.

# Note : Complete the task in constant time and space complexity.

# Constraints:
# 1 <= T <= 105
# -103 <= a <= 103
# -103 <= b <= 103
# -103 <= c <= 103

# Example:
# Input:
# 3
# 1 -2 1
# 1 -7 12
# 1 4 8

# Output:
# 1 1
# 4 3
# Imaginary


#User function Template for python3


##Complete this function
def quadraticRoots(a,b,c):
    #Your code here
    d = math.floor((b**2) - (4*a*c))
    if (d<0):
        print('Imaginary')
    else:
        root1 = math.floor(((-b + math.sqrt(d)) / (2.0 * a)))
        root2 = math.floor(((-b - math.sqrt(d)) / (2.0 * a)))
        if(root1>root2):
            print('{0} {1}'.format(root1,root2))
        else:
            print('{0} {1}'.format(root2,root1))
    




#{ 
#Driver Code Starts.

def main():
    
    T=int(input())
    
    while(T>0):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        
        quadraticRoots(a,b,c)
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends