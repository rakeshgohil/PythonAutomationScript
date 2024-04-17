from math import log, sqrt, exp
from scipy.stats import norm

def bsm_option_price(S, K, days_to_expiry, r, sigma, option_type):
    T = days_to_expiry / 365.0  # Convert days to years
    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    
    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Choose 'call' or 'put'.")
    
    return option_price

# Input parameters
S = 22519.40  # Current price of the underlying asset
K = 22850  # Strike price of the option
days_to_expiry = 6  # Time to expiration in days
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Implied volatility

# Calculate call option price
call_price = bsm_option_price(S, K, days_to_expiry, r, sigma, 'call')
print("Call option price:", call_price)

# Calculate put option price
put_price = bsm_option_price(S, K, days_to_expiry, r, sigma, 'put')
print("Put option price:", put_price)

