# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
# Easy

# 34

# 51

# Add to List

# Share
# Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.

# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

 

# Example 1:

# Input: s = "?zs"
# Output: "azs"
# Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
# Example 2:

# Input: s = "ubv?w"
# Output: "ubvaw"
# Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
# Example 3:

# Input: s = "j?qg??b"
# Output: "jaqgacb"
# Example 4:

# Input: s = "??yw?ipkj?"
# Output: "acywaipkja"

class Solution:
    def modifyString(self, s: str) -> str:
        r=""
        N=len(s)
        for i,j in enumerate(s):
            if j=="?":
                prev=i > 0 and r[i-1]=="a"
                nexts=i+1<N and s[i+1]=="a"
                
                if prev or nexts:
                    prevs=i>0 and r[i-1]=="b"
                    nextm=i+1<N and s[i+1]=="b"
                    
                    if prevs or nextm:
                        r+="c"
                        continue
                    r+="b"
                    continue
                r+="a"
            else:
                r+=j
        return r