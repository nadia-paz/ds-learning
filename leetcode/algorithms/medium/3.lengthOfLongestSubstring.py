"""
Given a string s, find the length of the longest 
substring without repeating characters.
"""


def lengthOfLongestSubstring(s: str) -> int:
    # list to keep not repeating element
    sub_s = []
    # length of sub_s
    length = 0
    # maximum length of the sub_s
    max = 0
    for ch in s:
        if ch not in sub_s:
            sub_s.append(ch)
        else:
            # if the element is already in the substring
            # calculate its length
            length = len(sub_s)
            # check if beats the previous maximum
            max = length if length > max else max
            # find the index of the repeating element in the substring
            i = sub_s.index(ch)
            # slice the substring from the next index 
            sub_s = sub_s[i+1:]
            # append the current character
            sub_s.append(ch)
            
    length = len(sub_s)
    max = length if length > max else max
    return max


print(lengthOfLongestSubstring("ababcdrat"))  
print(lengthOfLongestSubstring("pwwkew")) 
print(lengthOfLongestSubstring("abcabcbb")) 
print(lengthOfLongestSubstring("aab")) 