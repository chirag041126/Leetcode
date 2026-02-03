class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        # 1️⃣ Find p (increasing)
        p = 1
        while p < n and nums[p] > nums[p-1]:
            p += 1
        p -= 1

        if p == 0:
            return False

        # 2️⃣ Find q (decreasing)
        q = p + 1
        while q < n and nums[q] < nums[q-1]:
            q += 1
        q -= 1

        if q <= p or q == n-1:
            return False

        # 3️⃣ Check increasing again
        for i in range(q+1, n):
            if nums[i] <= nums[i-1]:
                return False

        return True
s=Solution()
print(s.isTrionic([1,3,5,4,2,6,8]))  # output True