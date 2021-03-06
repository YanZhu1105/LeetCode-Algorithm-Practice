# Given an array A of non-negative integers, return an array consisting of all t
# he even elements of A, followed by all the odd elements of A. 
# 
#  You may return any answer array that satisfies this condition. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 5000 
#  0 <= A[i] <= 5000 
#  
#  
#  Related Topics 数组 
#  👍 162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j:
            while i < j and not (A[i] & 1): i += 1
            while i < j and (A[j] & 1): j -= 1
            A[i], A[j] = A[j], A[i]
        return A
# leetcode submit region end(Prohibit modification and deletion)
