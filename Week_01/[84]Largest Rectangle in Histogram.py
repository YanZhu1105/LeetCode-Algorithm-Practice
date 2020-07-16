# Given n non-negative integers representing the histogram's bar height where th
# e width of each bar is 1, find the area of largest rectangle in the histogram. 
# 
#  
# 
#  
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3
# ]. 
# 
#  
# 
#  
# The largest rectangle is shown in the shaded area, which has area = 10 unit. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [2,1,5,6,2,3]
# Output: 10
#  
#  Related Topics 栈 数组 
#  👍 796 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights +[0]
        stack = []
        stack.append(0)
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                curr_h = heights[stack.pop()]
                area = curr_h * (i - 1 - stack[-1])
                res = max(area, res)
            stack.append(i)
        return res
# leetcode submit region end(Prohibit modification and deletion)
