# Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

from collections import Counter
import string

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        consonants = set(string.ascii_lowercase) - vowels

        cnt = Counter(s)  

        max_vowel = max((cnt[ch] for ch in vowels), default=0)
        max_consonant = max((cnt[ch] for ch in cnt if ch in consonants), default=0)

        return max_vowel + max_consonant
