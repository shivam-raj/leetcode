class Solution:
    def twoSum(self, x: List[int], target: int) -> List[int]:
        l,r = 0, len(x)-1
        while r>l:
            if x[l]+x[r]>target:
                r-=1
                continue
            elif x[l]+x[r]<target:
                l+=1
                continue
            else:
                return [l+1,r+1]

        