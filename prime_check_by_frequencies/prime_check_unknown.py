def frecuencia_formula_1(a): return 2 * a + 3
def frecuencia_formula_2(a): return (2 * a + 3) * 2 + (-1) ** a
def frecuencia_formula_3(a): return (6 * a + 9 + (-1) ** a) // 2

def b_mas(a): return 6 * a + 1
def b_menos(a): return 6 * a - 1

def is_prime_by_frequencies(X, a_max=100000):
    b_max = 0
    for a in range(1, a_max):
        for f in [frecuencia_formula_1, frecuencia_formula_2, frecuencia_formula_3]:
            freq = f(a)
            for base_func in [b_mas, b_menos]:
                b = base_func(a)
                b_max = max(b_max, b)
                if b < X < b ** 2 and (X - b) % freq == 0:
                    return "composite"
    # Verificar si se alcanzó b^2 > X en algún momento
    if b_max ** 2 > X:
        return "prime"
    else:
        return "unknown"

# Example usage
if __name__ == "__main__":
    X = int(input("Enter a number to check: "))
    result = is_prime_by_frequencies(X)
    print(result)
