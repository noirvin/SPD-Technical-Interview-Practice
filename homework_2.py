"""Leet Code Problem: Power Function
Implement pow(x, n), which calculates x raised to the power n .

Restated: Simplify the power function into a simpler form which returns x to the power of n
Clarifying Questions: Could x be a negative number?
Assumptions: x is going to be a 32 bit integer
rationale: used iterative multiplication to simplify power function, if n is negative the answer will be 1 over the result of iteration
suggested optimization:
"""

"""Restated: I'm going to take a positive or negative integer, and reverse the digits.

Clarifying Questions: If a reverse of a number starts with zero, do we keep it?

State Assumptions: I'm assuming integers with one digit are the same as their reverse.

Explain Rationale: I converted the integer to a string so i could treat it as an iterable with substrings being the value of each index,
then I added each substring from the last character of the word into a new string to reverse it

suggested improvement: make it work with fraction powers and imaginary numbers
"""
def pow_func(x,n):

    multiply=1
    counter = abs(n)
    while counter!=0:
        multiply*=x
        counter-=1
    if '-' in str(n):
        return 1/multiply
    else:
        return multiply




def reverse(num):

    str_num = str(num)

    if len(str_num)<2:
        return num
    else:
        sign = '-'
        negative = None
        reverse = ''
        if sign in str_num:
            negative = True
            str_num=str_num.replace(sign,'')
            counter = len(str_num)-1
            while counter>=0:
                reverse+=str_num[counter]
                counter-=1
        if negative:
            negative_reverse = sign+reverse
            return negative_reverse
        else:
            counter = len(str_num)-1
            while counter>=0:
                reverse+=str_num[counter]
                counter-=1
            return int(reverse)
test1 = 1
test2 = -2
test3 = 42
test4 = -42
print(reverse(test1))
print(reverse(test2))
print(reverse(test3))
print(reverse(test4))
print(pow_func(4,3))
print(pow_func(4,-3))
