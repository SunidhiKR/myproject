def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


def calculate_compound_interest(principal, rate, time):
    """Calculates compound interest."""
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    return interest


# Read input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (%): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)
print("Simple Interest:", simple_interest)

# Calculate compound interest
compound_interest = calculate_compound_interest(principal, rate, time)
print("Compound Interest:", compound_interest)
