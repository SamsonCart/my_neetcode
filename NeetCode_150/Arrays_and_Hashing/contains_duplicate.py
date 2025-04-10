class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    This solution uses a hash set to keep track of the numbers we have seen so far. If we see a number that is already in the set, we return True. 
    If we finish iterating through the list without finding any duplicates, we return False.
    
    Initially I had thought to use brute force for this solution, which would be O(n^2) time complexity, but I realized that using a hash set 
    would be much more efficient. However, the space complixty for hte brute force solution would have been O(1), so it would really depend on the
    size of the input list.
   
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    """