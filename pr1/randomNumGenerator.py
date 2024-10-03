import numpy as np

def random_logarithmic_number(base=10, min_value=1, max_value=1000):
    # Generate a uniform random number
    U = np.random.uniform(0, 1)
    
    # Apply the logarithmic transformation
    value = min_value * (max_value / min_value) ** U
    
    return value

# Generate a random logarithmic number
random_number = random_logarithmic_number(min_value=1, max_value=200)
print(f"Random logarithmic number: {random_number}")