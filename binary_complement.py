# Description from leetcode.com:
#   Given a positive integer, output its complement number. 
#   The complement strategy is to flip the bits of its binary representation.

# Note:
#   The given integer is guaranteed to fit within the range of a 32-bit signed integer.
#   You could assume no leading zero bit in the integer’s binary representation.

# Example 1:
#   Input: 5
#   Output: 2
#   Explanation: The binary representation of 5 is 101 (no leading zero bits), 
#   and its complement is 010. So you need to output 2.

# Example 2:
#   Input: 1
#   Output: 0
#   Explanation: The binary representation of 1 is 1 (no leading zero bits), 
#   and its complement is 0. So you need to output 0.

import numpy as np
import pandas as pd

# Auxiliary functions:

def to_binary(num):
    # takes in an integer and returns the binary version as a string
    a = bin(num)
    return a.split('b')[1]

def complement(bnry):
    # takes in a binary string and returns the complement of the string e.g. 101 -> 010
    cmp = ''
    for i in bnry:
        if i == '0':
            cmp += '1'
        else:
            cmp += '0'
    return cmp

def to_integer(str):
    # takes in a binary string and converts to and returns the equivalent integer
    my_int = 0
    exp = 0
    for i in reversed(str):
        my_int += (int(i)*(2**exp))
        exp += 1
    return my_int
      
    
# MAIN code:

user_int = int(input('Enter a non-negative integer: '))
user_bin = to_binary(user_int)
comp_bin = complement(to_binary(user_int))
comp_int = to_integer(comp_bin)

df = pd.DataFrame([[user_int,user_bin],[comp_int,comp_bin]],\
                  index="Original Complement".split(),columns="Integer Binary".split())
display(df)