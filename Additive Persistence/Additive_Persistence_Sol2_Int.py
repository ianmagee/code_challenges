# Solution 2: leave input as integer, don't convert to string (INTERMEDIATE)

def sumdigits(num,sum=0):
    # takes in an integer and returns the sum of the digits
    while num>0:
        i = num%10
        sum = sum + i
        num = (num - i)//10
    return (sum)

def howmany(num, count=1):
    # takes in an integer and returns its additive persistence value 
    tot = sumdigits(num)
    # while keeping count, recursively adds digits of each total until total is less than 10
    if tot >= 10:
        return (howmany(tot,count+1))
    return count

user_num = int(input("Enter a positive integer: "))

print(f'The additive persistence of {user_num} is {howmany(user_num)}.')
