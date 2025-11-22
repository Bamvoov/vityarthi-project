#question 5
def legendre_symbol(a, p):
    if p <= 2 or p % 2 == 0:
        raise ValueError("p must be an odd prime")
    
    if a % p == 0:
        return 0  # Legendre symbol is 0 if a is divisible by p
    
    exponent = (p - 1) // 2
    result = pow(a, exponent, p)
    if result == 1:
        return 1
    elif result == p - 1:
        return -1
    else:
        raise ValueError(f"Unexpected result: {result}")

if __name__ == "__main__":
    test_cases = [
        (2, 7), 
        (3, 11),  
        (5, 13),  
        (7, 17),   
        (4, 11), 
    ] 
    for a, p in test_cases:
        symbol = legendre_symbol(a, p)
        print(f"({a}/{p}) = {symbol}")
    
    print("\nVerification with known quadratic residues:")
    p = 19
    quadratic_residues = set(x*x % p for x in range(p))
    for a in range(p):
        symbol = legendre_symbol(a, p)
        is_residue = a in quadratic_residues
        expected = 1 if a != 0 and is_residue else (0 if a == 0 else -1)
        print(f"({a}/{p}) = {symbol} (expected: {expected})")
