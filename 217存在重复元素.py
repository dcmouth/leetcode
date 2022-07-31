"""
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:
输入: [1,2,3,1]
输出: true
示例 2:
输入: [1,2,3,4]
输出: false
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashdict = {}
        for i in nums:
            if hashdict.get(i) is None:
                hashdict[i] = 1
            else:
                hashdict[i] += 1

        
        #另外一种方法 set()的时间复杂度是O(1)或者是O(n)很小的
        #return len(nums) > len(set(nums))

        
        

nums = [1,2,3,1]
a = Solution()
print(a.containsDuplicate(nums))

print("github上增加的部分")
