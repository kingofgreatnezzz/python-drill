# Arithmetic, divmod, rounding, Decimal
# 1. Average of 5 numbers with a loop, then with sum()/len().
# Check: Both give the same value.

num = [1,2,3,4,5]

# 2. Use divmod to convert 3725 seconds to h:m:s.
# Check: 1h 2m 5s.
hour, sec = divmod(2345, 60)
print(hour, sec)

# 3. Run round(2.675, 2). Explain the result, then fix with Decimal and ROUND_HALF_UP.
# Check: Float gives 2.67; Decimal gives 2.68.
print(round(2.345,2))

# 4. Write is_prime(n). List primes under 30.
# Check: 2,3,5,7,11,13,17,19,23,29.
def is_prime(n):
    for i in range(1,30):
        if n%i == 0:
            print(n)

# 5. Compound interest: P=1000, r=5%, 10 years using **.
#Check: 1628.89 (rounded to 2 dp).