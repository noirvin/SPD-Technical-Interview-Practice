'''
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.
'''
def is_pal_int(num):

    #check edge case
    if num is not None:
        #set right and left pointer
        right = len(str(num))-1
        left = 0
        #iterate from both ends of the string to the middle and see
        #if characters match
        #if iteration is not interrupted, it's a palindrome
        while left<right:
            #in case it's a boring word
            if str(num)[left]!=str(num)[right]:
                return False
            else:
                right-=1
                left+=1
        return True
    else:
        return None

'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
def remove(nums,val):

    #iterate over list and extract target elements equivalent to val
    index=0
    while index<len(nums)-1:
        if nums[index] == val:
            #delete target
            nums.pop(index)
        else:
            index+=1

    #new length
    return len(nums)


test_array=[1,1,1,2,2,4,3,8]
remove(test_array,1)
print(test_array)
remove(test_array,2)
print(test_array)





test = None
test2 = 1234321
test3 = 12432875
print(is_pal_int(test), is_pal_int(test2), is_pal_int(test3))
