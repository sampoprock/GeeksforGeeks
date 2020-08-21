# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.
# Your Task:
# You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

# Expected Time Complexity: O(N*Log(N)).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= N <= 104
# -1000 <= A[i] <= 1000, for each valid i


#Your task is to complete this function
#Your should return the required output
def maxLen(n, arr):
    #Code here
    sumM={}
    maxLen=0
    soFar=0
    
    for i in range(n):
        soFar+=arr[i]
        
        if arr[i] is 0 and maxLen is 0:
            maxLen=1
        if soFar is 0:
            maxLen=i+1
        if soFar in sumM:
            maxLen=max(maxLen,i-sumM[soFar])
        else:
            sumM[soFar]=i
    return maxLen



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends