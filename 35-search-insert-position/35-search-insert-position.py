class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:   
        #Sets lower value to star search
        low = 0
        #Sets higher vvalue to find middle
        high = len(nums) - 1
        
        while low <= high:
            #Gets the middle of the list
            middle = (low + high) // 2
            #Checks if number in middle is equal to target
            if nums[middle] == target:
                return middle
            #if middle lower than target, add one to middle to check right part of the list
            elif nums[middle] < target:
                low = middle + 1
            #if middle higher than target, subtract one to check left part of the list
            else:
                high = middle - 1
        return low