#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution(object):
    def merge_sort(self,nums):
        
        if len(nums)<=1:
            return nums
        
        elif len(nums)>1:
            star=[]
            n=len(nums)
            mid=int(n//2)
            left=self.merge_sort(nums[:mid])
            right=self.merge_sort(nums[mid:])
            
        a=0#左邊的第零號位置
        b=0#右邊第零號位置
        
        while a<len(left) and b<len(right):
            if left[a] > right[b]:
                star.append(left[a])
                a+=1
            else:
                star.append(right[b])
                b+=1
                
        star+=left[a:]
        star+=right[b:]
        return star       
               
    


# In[4]:


nums=[-5,28,34,99,11,67,0,-53,20] 
out = Solution().merge_sort(nums)
out


# In[ ]:




