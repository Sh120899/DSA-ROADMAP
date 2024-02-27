#!/usr/bin/env python
# coding: utf-8

# # ARRAY
# ## 1. Two Sum problem
# 

# In[1]:


##

def twosum(nums,target):
    hashmap={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[n]=i
    return

numbers=[2,1,5,3]
target=4
ans=twosum(numbers,target)
print(ans)


# In[48]:


arr=[4,5,0,-2,-3,1]
k = 5
for i in range(len(arr)):
    for j in range(i+1):
        if sum(arr[j:i+1])%k==0:
            print(arr[j:i+1],end=" ")
    print()


# In[7]:


def divisiblecount(nums,k):
    hashmap = {}
    count, presum = 0, 0
    hashmap[0] = 1
    for num in nums:
        presum += num
        reminder = presum % k
        if reminder < 0:
            reminder +=k
        if reminder in hashmap:
            count +=hashmap[reminder]
            hashmap[reminder] +=1
        else:
            hashmap[reminder] =1
    return count
    


arr=[6]
k = 1
print(divisiblecount(arr,k))


# In[ ]:





# In[ ]:




