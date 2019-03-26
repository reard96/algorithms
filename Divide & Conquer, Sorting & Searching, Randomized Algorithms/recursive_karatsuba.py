def karat(x, y):
    # Base case
    if x < 10 and y < 10:
        # i.e. if x and y are both single digits
        return x * y

    # Recursive steps
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)
    c = y // (10 ** m)
    d = y % (10 ** m)

    ac = karat(a, c)
    bd = karat(b, d)
    abcd = karat(a+b, c+d) - ac - bd

    # Write n as m*2 to control for both even and odd n
    return ac * (10 ** (m * 2)) + abcd * (10 ** m) + bd

# Tests: the below 2 should return the same number
print(karat(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))

print(3141592653589793238462643383279502884197169399375105820974944592
 * 2718281828459045235360287471352662497757247093699959574966967627)
