# 859. Buddy Strings
# Easy

# 679

# 469

# Add to List

# Share
# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false
 

# Constraints:

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist of lowercase letters.



class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B) or set(A)!=set(B): return False
        
        if A==B:
            return len(A) - len(set(A)) >=1
        else:
            index=[]
            counter=0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    index.append(i)
                if counter > 2:
                    return False
            return A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]]
        