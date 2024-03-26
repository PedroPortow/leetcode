# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        max_substring_length = 0
        for char in range(0, len(s)):
            current_char = s[char]

            if current_char in substring:
                current_substring_length = len(substring)

                if current_substring_length > max_substring_length:
                    max_substring_length = current_substring_length

                substring = [current_char]
                continue

            substring.append(current_char)

        return max_substring_length

solution = Solution()
s1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(s1))
s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))
s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))
