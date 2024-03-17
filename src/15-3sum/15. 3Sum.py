def twosum(nums: list[int], l, out):
    i = l + 1
    j = len(nums) - 1
    while i < j:
        c = nums[l] + nums[i] + nums[j]
        if c > 0:
            j -= 1
        elif c < 0:
            i += 1
        else:
            out.append([nums[l], nums[i], nums[j]])
            i += 1
            j -= 1
            while i < j and nums[i] == nums[i-1]:
                i += 1
    return out


class Solution:
    def threeSumBack(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        s = sorted(nums)
        for l in range(n):
            if s[l] > 0:
                break
            if l == 0 or s[l] != s[l-1]:
                twosums = twosum(s, l, out)
        return out

    def threeSum(self, a) -> list[list[int]]:
        out = set()
        dups = set()
        n = len(a)
        for i, l in enumerate(a):
            seen = set()
            if l in dups:
                continue
            dups.add(l)
            complement = -l
            # we need m and r to add to complement
            for j in range(i+1, n):
                final = complement - a[j]
                if final in seen:
                    out.add(tuple(sorted([l, a[j], final])))
                seen.add(a[j])
        return out
