# SOLUTION 1: convert to string first (EASY)

def addup(n,count=1):
    # takes an integer input, adds up the digits by converting it to a string,
    # then returns the additive persistence
    tot = sum(int(i) for i in str(n))
    # keeps count and continues calling function recursively until total is less than 10
    if tot>=10:
        return(addup(tot,count+1))
    return count

num = int(input("Enter a positive integer: "))
ap = addup(num)
print(f'The additive persistence of {num} is {ap}.')