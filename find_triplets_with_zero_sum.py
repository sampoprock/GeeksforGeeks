# Given an array of integers. Check whether it contains a triplet that sums up to zero. 

# Example 1:

# Input: N = 5, arr[] = {0, -1, 2, -3, 1}
# Output: true
# Explanation: 0, -1 and 1 forms a triplet
# with sum equal to 0.
# Example 2:

# Input: N = 3, arr[] = {1, 2, 3}
# Output: false
# Explanation: No triplet with zero sum exists. 

# Your Task:
# You don't need to read input or print anything. Your task is to complete the boolean function findTriplets() which takes the array arr[] and the size of the array (n) as inputs and returns True if the given array has a triplet with zero sum and False otherwise. 

# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(1)

# Constrains:
# 1 <= N <= 104
# -106 <= Ai <= 106


#User function Template for python3
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in arr[], else return 0'''
    
def findTriplets(arr,n):
    #code here
    arr.sort()
    for i in range(n-2):
        
        if i>0 and arr[i]==arr[i-1]:
            continue
        left=i+1
        right=n-1
        while(left<right):
            total=arr[i]+arr[left]+arr[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                return 1
                
                
                left+=1
                right-=1
                
    return 0
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        print(findTriplets(a,n))
# } Driver Code Ends