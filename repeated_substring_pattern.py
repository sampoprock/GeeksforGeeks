# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

# Example 1:

# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# Example 2:

# Input: "aba"
# Output: False
# Example 3:

# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub=''
        
        for i in range(len(s)//2):
            sub+=s[i]
            if len(s) % len(sub) == 0:
                if sub * (len(s) // len(sub))==s:
                    return True
        return False