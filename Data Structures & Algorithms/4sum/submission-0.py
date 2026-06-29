class Solution:
    def fourSum(self, nums, target):

        nums.sort()     # SORT the array since we are not interested in order

        ans = []
        n = len(nums)
        for j in range(n - 3):
            if j > 0 and nums[j] == nums[j - 1]: #Skipping duplicates
                continue

            for i in range(j + 1, n - 2):
                req = nums[i] + nums[j]  #at this point i and j are fixed

                if i > j + 1 and nums[i] == nums[i - 1]: #Skipping duplicates
                    continue

                L = i + 1                  #O(n) part
                R = n - 1

                while L < R:               # 2 pointer O(n)

                    s = nums[L] + nums[R] + req

                    if s < target:
                        L += 1

                    elif s > target:
                        R -= 1

                    else:
                        ans.append([nums[j], nums[i], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L - 1]:  #avoiding copies
                            L += 1
                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1

        return ans