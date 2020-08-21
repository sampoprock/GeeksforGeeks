# You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. The transition point is a point where "0" ends and "1" begins (0 based indexing).
# Note that, if there is no "1" exists, print -1.
# Note that, in case of all 1s print 0.

# Example 1:

# Input:
# N = 5
# C[] = {0,0,0,1,1}
# Output: 3
# Explanation: position 3 is 0 and next
# one is 1, so answer is 3.
# Example 2:

# Input:
# N = 4
# C[] = {0,0,0,0}
# Output: -1
# Explanation: Since, there is no "1",so
# the answer is -1.
# Your Task:
# The task is to complete the function transitionPoint() that takes array and N as input and returns the value of the position where "0" ends and "1" begins.

# Expected Time Complexity: O(LogN).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 ≤ N ≤ 500000
# 0 ≤ C[i] ≤ 1

# your task is to complete this function
# finvtion should return an integer
def transitionPoint(arr, n):
    #Code here
    if arr[0]==1:
        return 0
    l=0
    r=n-1
    while(l<=r):
       mid=(l+r)//2
       if(arr[mid]==0):
           l=mid+1
       elif (arr[mid]==1):
           if arr[mid-1]==0:
               return mid
           r=mid-1
    return -1


#{ 
#  Driver Code Starts

#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends
