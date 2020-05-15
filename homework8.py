'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Complexity: this function requires conversion of string to int and back to int, So O(n)
'''
def binary_sum(a,b):

    sum = int(a,2)+int(b,2)
    str_prepared = str(bin(sum)).replace('0b','')

    return str_prepared
test = ['11','1']
test2= ['1010','10111']

print(binary_sum(test[0],test[1]))
print(binary_sum(test2[0],test2[1]))
