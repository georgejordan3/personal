'''
Factorial
'''
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

'''
Combinations
'''
def combinations(n, k):
    return int(factorial(n) / (factorial(n - k) * factorial(k)))

'''
Binomial Probability Mass Function
'''
def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

'''
Cumulative Distribution Function
'''
def binomial_cdf(n, k_high, p = .5):
    cumulative = 0.0
    for k in range(k_high + 1):
        cumulative += binomial_pmf(n, k, p)
    return cumulative

'''
Using Binomial Distribution with Dictionaries
'''
def binomial_pmf_dict(n, k_low, k_high, p = .5):
    d = dict()
    for k in range(k_low, k_high + 1):
        d[k] = binomial_pmf(n, k, p)
    return d

d = binomial_pmf_dict(12, 0, 12, p=.5)
for k, v in d.items():
    print(f'{k}: {v}')

'''
Poisson PMF
'''
def poisson_pmf(lmbda, k):
    return lmbda ** k * e ** (-lmbda) / factorial(k)

'''
Poisson CDF
'''
def poisson_cdf(lmbda, k_high):
    cdf = 0.0
    for k in range(0, k_high + 1):
        cdf += poisson_pmf(lmbda, k)
    return cdf

'''
Poisson PMF Dictionary
'''
def poisson_pmf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k + 1):
        d[k] = poisson_pmf(lmbda,k)
    
    return d
    
for k, v in d.items():
    print(f'{k}: {v}')

'''
Poisson CDF Dictionary
'''
def poisson_cdf_dict(lmbda, low_k, high_k):
    d = dict()
    for k in range(low_k, high_k + 1):
        d[k] = poisson_cdf(lmbda, low_k, high_k)
    return d

for k, v in d.items():
    print(f'{k}: {v}')

'''
Geometric PMF
'''
def geometric_pmf(p, k, inclusive = True):
    if inclusive:
        return p * (1 - p) ** (k - 1)
    else:
        return p * (1 - p) ** k

'''
Geometric CDF w/ Accumulator
'''
def geom_cdf_accum(p, k, inclusive = True):
    proba_ = 0

    if inclusive == True:
        starting_at = 1
    else:
        starting_at = 0

    for r in range(starting_at, k + 1):
        proba_ += geometric_pmf(p, r, inclusive)

    return proba_

'''
Geometric CDF Closed
'''
def geom_cdf_closed(p, k, inclusive = True):
    if inclusive:
        return 1 - (1 - p) ** k
    else:
        return 1 - (1 - p) ** (k + 1)

'''
Geometric PMF Dictionary
'''
def geometric_pmf_dict(p, k_high, inclusive = True):
    d = dict()

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0

    for k in range(starting_at, k_high + 1):
        d[k] = geometric_pmf(p, k, inclusive)
    
    return d

'''
Geometric CDF Dictionary
'''
def geometric_cdf_dict(p, k_high, inclusive = True):
    d = dict()

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0

    for k in range(starting_at, k_high + 1):
        d[k] = geom_cdf_closed(p, k, inclusive)
    
    return d

'''
Performing a Geometric Trial with Bernoulli
'''
from random import random

def bernoulli(p = 0.5):
    if random() < p:
        return 1
    else:
        return 0

def perform_geometric(p = 0.5):
    num_trials = 0
    for _ in range(2000000):
        flip = bernoulli(p)
        num_trials += 1
        
        print(f'Trial: {flip}')
        if flip == 1:
            break
    print(f'Success on the {num_trials} trial')

perform_geometric(p)