class Solution:
    def threeSum(self, nums):

        nums.sort()

        ans = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1

            while L < R:

                s = nums[i] + nums[L] + nums[R]

                if s < 0:
                    L += 1

                elif s > 0:
                    R -= 1

                else:
                    ans.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        return ans