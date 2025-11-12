class Solution(object):
    def firstMissingPositive(self, nums):
        nums = [x for x in nums if x > 0]  
        nums.sort()

        var1 = 1
        for n in nums:
            if n == var1:
                var1 += 1   # found it, look for next
            elif n > var1:
                break       # gap found

        return var1


# Example
arr = [7,8,9,11,12]
a1 = Solution()
print(a1.firstMissingPositive(arr))  