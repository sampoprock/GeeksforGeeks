# # 859. Buddy Strings
# # Easy

# # 679

# # 469

# # Add to List

# # Share
# # Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

# # Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

# # Example 1:

# # Input: A = "ab", B = "ba"
# # Output: true
# # Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
# # Example 2:

# # Input: A = "ab", B = "ab"
# # Output: false
# # Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
# # Example 3:

# # Input: A = "aa", B = "aa"
# # Output: true
# # Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
# # Example 4:

# # Input: A = "aaaaaaabc", B = "aaaaaaacb"
# # Output: true
# # Example 5:

# # Input: A = "", B = "aa"
# # Output: false
 

# # Constraints:

# # 0 <= A.length <= 20000
# # 0 <= B.length <= 20000
# # A and B consist of lowercase letters.



# class Solution:
#     def buddyStrings(self, A: str, B: str) -> bool:
        
#         if len(A) != len(B) or set(A)!=set(B): return False
        
#         if A==B:1608. Special Array With X Elements Greater Than or Equal X
# Easy

# 117

# 15

# Add to List

# Share
# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

# Notice that x does not have to be an element in nums.

# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

# Example 1:

# Input: nums = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
# Example 2:

# Input: nums = [0,0]
# Output: -1
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.
# Example 3:

# Input: nums = [0,4,3,0,4]
# Output: 3
# Explanation: There are 3 values that are greater than or equal to 3.
# Example 4:

# Input: nums = [3,6,7,7,0]
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#             return len(A) - len(set(A)) >=1
#         else:
#             index=[]
#             counter=0
#             for i in range(len(A)):
#                 if A[i] != B[i]:
#                     counter += 1
#                     index.append(i)
#                 if counter > 2:
#                     return False
#             return A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]]
        




class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        for i in range(0,1001):
            count=0
            for j in nums:
                if j>=i:
                    count+=1
            if count==i:
                return i
        return -1