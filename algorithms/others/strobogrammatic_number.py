# Strobogrammatic Number III
# Find all strobogrammatic numbers that are of length = n.
# f(2) => ["11","69","88","96"] ("00" does not count)
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        memo = { 0: [''], 1:  ['0', '1', '8'] }
        return self.dfs(n, n, memo)

    # m - current n, n - target n
    def dfs(self, m, n, memo):
        if m in memo: return memo[m]

        result = []
        nums = self.dfs(m - 2, n, memo)

        for num in nums:
            for pair in ['00', '11', '69', '88', '96']:
                if m == n and pair == '00':
                    continue
                result.append(pair[0] + num + pair[1])

        memo[m] = result
        return result


# Strobogrammatic Number III
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# Input: low = "50", high = "100"
# Output: 3
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.

# note: a valid number with leading 0 can only 0 itself
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        memo = { 0: [''], 1:  ['0', '1', '8'] }
        lo_n, hi_n = len(low), len(high)

        # to cover both even/odd lengths
        self.dfs(hi_n - 1, hi_n - 1, memo)
        self.dfs(hi_n, hi_n, memo)

        count = 0
        for n, nums in memo.iteritems():
            if n < lo_n or n > hi_n:
                continue
            for num in nums:
                if len(num) > 1 and num[0] == '0':
                    continue
                if n == lo_n or n == hi_n:
                    if int(num) < int(low) or int(num) > int(high):
                        continue
                count += 1

        return count

    def dfs(self, m, n, memo):
        if m in memo: return memo[m]

        res = []
        nums = self.dfs(m - 2, n, memo)

        for num in nums:
            for pair in ['00', '11', '69', '88', '96']:
                # filter numbers with leading 0 in the main function
                res.append(pair[0] + num + pair[1])

        memo[m] = res
        return res
