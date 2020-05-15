'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Complexity: this function requires conversion of string to int and back to int, So O(n)
'''
def binary_sum(a,b):

    sum = int(a,2)+int(b,2)
    str_prepared = str(bin(sum)).replace('0b','')

    return str_prepared

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Complexity: O(n^2) since there is a nested while loop
'''

def two_sum(nums, target):
    indices=[]
    i=0
    j=i

    while i<= len(nums)-1:

        while j<=len(nums)-1:

            if nums[i]+nums[j]==target:
                indices.append(i)
                indices.append(j)
                return indices
            else:
                j+=1
        i+=1
    return "valid indices not found"


test = ['11','1']
test2= ['1010','10111']

print(binary_sum(test[0],test[1]))
print(binary_sum(test2[0],test2[1]))

two_sum_list = [2,7,11,15]

print(two_sum(two_sum_list,9))
