nums = [2,7,11,15]
target = 9
def twosum(nums,target):
    seen={}
        

    for key,value in enumerate(nums):

        ans=target - value
        
        if ans  in seen:
            return [seen[ans],key]

        seen[value]=key
    
    return []

def twosum(nums,target):
    seen={}
    

    for key,value in enumerate(nums):

        ans=target - value
        
        if ans  in seen:
            return [seen[ans],key]

        seen[value]=key
    
    return []
   


#twosum(nums,target)
print(twosum(nums,target))