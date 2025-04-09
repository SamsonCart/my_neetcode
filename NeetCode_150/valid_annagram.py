class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        if countS == countT:
            return True
        else:
            return False
        
"""
Neetcode Link: https://neetcode.io/problems/is-anagram

Description: This problem takes in two words and determines if they are annagrams of one another,
meaning they are the same word but with the letters in a different order.
The solution is to use a hash map to count the number of times each letter 
appears in each word and then compare the two hash maps.

Time Complexity: O(n + m)
Space Complexity: O(1) since we have, at most, 26 characters

Lessons: I needed to remember that there was an inital check on this, even before it is sorted. 
If the length of the strings aren't the same, then of course it isn't an anagram. 
"""