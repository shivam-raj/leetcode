class Solution:
    def threeSum(self, x: List[int]) -> List[List[int]]:
        res=[]
        x.sort()
        for i in range(len(x)):
            if i>0 and x[i] == x[i-1]:
                continue

            j=i+1
            k=len(x)-1

            while k>j:
                total = x[i]+x[j]+x[k]
                if total>0:
                    k-=1
                    continue 
                elif total<0:
                    j+=1
                else:
                    res.append([x[i],x[j],x[k]])
                    j+=1

                    while x[j] == x[j-1] and j<k:
                        j+=1
        return res

