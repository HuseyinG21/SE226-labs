# --------- GLOBAL VARIABLE ---------
total_sum = 0


# --------- QUESTION 1 ---------
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


# --------- QUESTION 2 ---------
def exp_x(x, n):
    abs_val = lambda t: t if t >= 0 else -t

    total = 0

    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)

        if i % 2 == 1:   # (-1)^i
            term = -term

        total += abs_val(term) if term < 0 else term

    return total


# --------- QUESTION 3 ---------
def geometric_series(n, r, current_power=0):
    """
    Recursive function to compute:
    G_n = 1 + r + r^2 + ... + r^n

    Logic:
    - Adds r^current_power in each call
    - Increases power step-by-step
    - Stops when current_power > n

    Sign:
    - No alternating sign
    - Depends only on r
    """

    global total_sum
 
    if current_power > n:
        return

    total_sum += r ** current_power
    geometric_series(n, r, current_power + 1)

# Question 2
x = float(input("Enter x: "))
n = int(input("Enter n: "))

print("Result:", exp_x(x, n))


# Question 3
n = int(input("Enter n: "))
r = float(input("Enter r: "))

geometric_series(n, r)
print("Geometric Sum:", total_sum)