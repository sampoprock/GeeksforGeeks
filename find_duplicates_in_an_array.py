# Find duplicates in an array Submissions: 46328   Accuracy: 20.69%   Difficulty: Easy   Marks: 2
# Associated Course(s):   Interview Preparation   Amazon SDE Test Series
                
# Problems
# Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

# Example 1:

# Input:
# N = 4
# a[] = {0,3,1,2}
# Output: -1
# Explanation: N=4 and all elements from 0
# to (N-1 = 3) are present in the given
# array. Therefore output is -1.
# Example 2:

# Input:
# N = 5
# a[] = {2,3,1,2,3}
# Output: 2 3 
# Explanation: 2 and 3 occur more than once
# in the given array.
# Your Task:
# Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in sorted manner. If no such element is found return -1. 

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(n).
# Note : The extra space is only for the array to be returned.
# Try and perform all operation withing the provided array. 

# Constraints:
# 1 <= N <= 105
# 0 <= A[i] <= N-1, for each valid i


def duplicates(arr, n): 

	for i in range(0, n): 
		index = arr[i] % n 
		arr[index] += n 
		
	flag=False
	res = []
	for i in range(0,n): 
		if (arr[i]//n) > 1: 
			res.append(i)
			flag=True
	
	if flag==False:
	    res.append(-1)
	return res
	    



#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends