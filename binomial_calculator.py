# CREATING FUNCTIONS FROM SCRATCH TO IMPLEMENT BINOMIAL MODEL

def factorial(num):
    #Takes in a non-negative integer and returns the factorial value
    if num == 0 or num == 1:
        return (1)
    f = num
    for i in range(1,num):
        f *= i
    return (f)

def choose(n,k):
    #Takes in two integers, n and k, and returns how many possible combinations of k exist in n (n choose k)
    facn = factorial(n)
    fack = factorial(k)
    facnmink = factorial(n-k)
    nchoosek = facn/(fack*facnmink)
    return(int(nchoosek))

def binomialpdf(n,p,k):
    # Using a binomial model, returns the probability using trials(n), probability (p), and successes(k)
    q = 1 - p
    return(choose(n,k)*(p**k)*(q**(n-k)))

def binomialcdf(n,p,k):
    #Calculates and returns P(X≤k) for a binomial distribution using trials(n),probability(p),successes(k)
    cdf = 0
    for i in range(1,k+1):
        cdf += binomialpdf(n,p,i)
    return cdf   

def mean(n,p):
    #Calculates mean of a binomial distribution using trials(n) and probability(p)
    return n*p

def sd(n,p):
    #Calculates standard deviation of a binomial distribution
    return (n*p*(1-p))**(1/2)

def normalcheck(n,p):
    #Checks to see if normal model approximation is appropriate and returns boolean
    return ((n*p>=10) and (n*(1-p)>=10))

#MAIN

print('B I N O M I A L   D I S T R I B U T I O N')

while True:
    # Get user input for n and p, then verify that n is nonnegative integer and 0≤p≤1
    try:
        trials = int(input('Number of Trials (n):  '))
        prob = float(input('Probability of Success (p):  '))
        succ = int(input('Enter Number of Successes (k):  '))
    except:
        print('n must be nonnegative integer and p must be a real number between 0 and 1. Try again...')
        continue
    else:
        break



#binomial calculations
pdf = binomialpdf(trials,prob,succ)
cdf = binomialcdf(trials,prob,succ)
kminusone = binomialcdf(trials,prob,succ-1)
mu = mean(trials,prob)
sigma = sd(trials,prob)
filler = '----------------------------------'

print('\nMODEL        VALUE')
print(filler)
print(f'P(X={succ}) = {pdf}')
print(filler)
print(f'P(X≤{succ}) = {cdf}')
print(filler)
print(f'P(X<{succ}) = {kminusone}')
print(filler)
print(f'P(X>{succ}) = {1-cdf}')
print(filler)
print(f'P(X≥{succ}) = {1 - kminusone}')

print('\nBONUS:')
print(f'MEAN = {mu}')
print(f'STDEV = {sigma}')
# extra bonus: tells user if normal approximation is appropriate
if normalcheck(trials,prob):
    print('Normal Model Approximation is appropriate')