class Solution(object):
    
    def heap_sort(self,nums):
        
        n=len(nums)#nums的長度
        
        i=(n//2)-1#最後一個父節點
        
        for x in range(i,-1,-1):
             self.heapify(nums,x, n)  
                
        for x in range(n-1, 0, -1):   
            nums[x],nums[0]=nums[0],nums[x]#最大最小值位子交換 
            self.heapify(nums,0,x)
        return nums
    
    def heapify(self,nums,x,n):
        
        max=x
        
        left=2 * x + 1  
        right=2 * x + 2    
        
        if left < n and nums[x] < nums[left]:   
            max = left  
        if right < n and nums[x] < nums[right]:   
            max = right   
        if max != x:   
            nums[x],nums[max]=nums[max],nums[x]   
            self.heapify(nums, max,n)  
        
            
a = [5,3,1,2,4]
out = Solution().heap_sort(a)
out
