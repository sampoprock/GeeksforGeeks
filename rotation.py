# RotationSubmissions: 50097   Accuracy: 22.44%   Difficulty: Easy   Marks: 2
          
# Problems
# Given a sorted array A of size N. The array is rotated 'K' times. Find the value of 'K'. The array may contain duplicate elements.

# Input:
# The first line contains an integer T, depicting total number of test cases. T testcases follow. Each testcase contains two lines of input. The first line contains an integer N depicting the size of array. The next line contains elements of the array separated by spaces.

# Output:
# For each testcase, print the value of K.

# Constraints:
# 1 <= T <= 100
# 1 <= N <=107
# 0 <= Ai <= 1018

# Example:
# Input
# 2
# 5
# 5 1 2 3 4
# 5
# 1 2 3 4 5
# Output
# 1
# 0

# Explanation:
# Testcase1: 5 1 2 3 4. The original sorted array is 1 2 3 4 5. We can see that the array was rotated 1 times to the right.




#code
def ans(a,start,end):
    mid= (start+end)//2
    
    if(start>=end):
        result=0
    elif a[mid]<a[mid-1]:
        result= mid
    elif a[mid]>a[mid+1]:
        result=mid+1
    else:
        if a[start]>a[mid]:
            result= ans(a,start,mid)
        elif a[start]<a[mid]:
            result=ans(a,mid+1,end)
        else:
            result=max(ans(a,start,mid),ans(a,mid+1,end))
    return result
    
    
t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    print(ans(li,0,n-1))