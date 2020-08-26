# You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

# Example 1:

# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.
# Example 2:

# Input:
# N = 7
# A[] = {86,39,90,67,84,66,62}
# x = 42, y = 12
# Output: -1
# Explanation: x = 42 and y = 12. We return
# -1 as x and y don't exist in the array.
# Your Task:
# Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum distance between x and y in the array. If no such distance is possible then return -1.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= N <= 105
# 0 <= A[i], x, y <= 105



def minDist(arr, n, x, y):
    # Code here
    i=0
    p=-1
    mini = 999999 
      
    for i in range(n):  
      
        if(arr[i] ==x or arr[i] == y): 
          
            if(p != -1 and arr[i] != arr[p]): 
                mini = min(mini,i-p) 
               
            p=i 
          
    if(mini == 999999): 
       return -1
    return mini
        
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(minDist(arr, n, x, y))



# } Driver Code Ends