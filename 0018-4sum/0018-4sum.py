class Solution:
    def fourSum(self, y: List[int], target: int) -> List[List[int]]:
        
        def twoSum(nums,req):
            ret = []
            l,r = 0,len(nums)-1
            while r>l:
                if nums[l]+nums[r]==req:
                    ret.append([nums[l], nums[r]])
                    l+=1
                    r-=1
                    while r>l and nums[l]==nums[l-1]:
                        l+=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l] + nums[r] < req:
                    l+=1
                else:
                    r-=1
            return ret
            
        
        y.sort()
        ans = set()
        print("y -> {}".format(y))

        matched = set()
        found = {}
        for i in range(len(y)-3):
            if not(i==0 or i>0 and y[i]!=y[i-1]):
                continue
            j=len(y)-1
            while j>i:
                if (y[i], y[j]) not in matched:
                    #print("({},{}) not in matched : {}".format(y[i],y[j],matched))
                    ntarget = target-1*(y[i]+y[j])
                    Y = list(y)
                    del Y[j]
                    del Y[i]
                    res=[]
                    if ntarget in found:
                        res=found[ntarget]
                    else:
                        res = twoSum(Y, ntarget)
                    #print("{},{} y[i]: {} y[j]: {} ntarget: {} res: {}".format(i,j,y[i],y[j],ntarget, res))
                    if len(res)>0:
                        for arr in res:
                            ans.add(tuple(sorted([y[i], y[j], arr[0], arr[1]])))
                    matched.add((y[i], y[j]))
                j-=1
        return [list(arr) for arr in ans]
            
        