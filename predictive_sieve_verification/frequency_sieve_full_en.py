"""
Frequency-based Sieve (Optimized)
---------------------------------
This function generates a list of prime numbers using a frequency-based model
derived from the 6n±1 pattern. It applies alternating steps (F1, F2) to cancel 
composite numbers by simulated collisions across frequency lanes.

The algorithm uses an indexed list and dictionary for faster cancellation 
marking within a predefined limit.
"""

def criba_frecuencias_excel_style_opt(limite, max_producto=10**6):
    """
    Optimized frequency sieve.
    Usa lista de números 6N±1, cancelación por índice,
    y acceso rápido por diccionario para grandes rangos.
    """
    def F2(n): return 2 * n + 3
    def F1(n): return 2 * (2 * n + 3) + (-1)**n
    def A(n): return (6 * n + 9 + (-1)**n) // 2

    lista_6np1 = [i for i in range(5, limite + 1) if i % 6 == 1 or i % 6 == 5]
    indices = {val: idx for idx, val in enumerate(lista_6np1)}
    longitud = len(lista_6np1)
    cancelado = np.zeros(longitud, dtype=bool)

    producto = 1
    tamaño_bloque = 0
    idx_n = 0

    while True:
        a_n = A(idx_n)
        if a_n > limite:
            break

        f1 = F1(idx_n)
        f2 = F2(idx_n)

        if producto * a_n > tamaño_bloque and producto * a_n <= max_producto:
            producto *= a_n
            tamaño_bloque = producto

        base_idx = indices.get(a_n, None)
        if base_idx is None:
            idx_n += 1
            continue

        pos = base_idx
        toggle = True
        while True:
            paso = f1 if toggle else f2
            pos += paso
            toggle = not toggle
            if pos >= longitud:
                break
            cancelado[pos] = True

        idx_n += 1

    primos = [2, 3] + [lista_6np1[i] for i in range(longitud) if not cancelado[i]]
    return primos



from math import isqrt

"""
Predictive Primality Checker
----------------------------
Given a number T, this function determines whether T is prime according to the 
frequency sieve model. It simulates the alternation of step patterns F1 and F2 
starting from each base A(n) until a collision (i.e., exact match) with T 
indicates that T is composite.
"""

def es_primo_por_frecuencias_corr(T):
    """
    Evaluates whether T is prime using the frequency sieve model.
    Follows the exact logic of the macro: alternating F1 and F2 from each base.
    """
    def F2(n): return 2 * n + 3
    def F1(n): return 2 * (2 * n + 3) + (-1)**n
    def A(n): return (6 * n + 9 + (-1)**n) // 2

    raiz_limite = isqrt(T)
    idx_n = 0

    while True:
        base = A(idx_n)
        if base > raiz_limite:
            break

        f1 = F1(idx_n)
        f2 = F2(idx_n)

        # Simulate the race track from the base position
        pos = base
        toggle = True
        while pos < T:
            paso = f1 if toggle else f2
            pos += paso
            toggle = not toggle

        if pos == T:
            return False, f"collision from base {base} using step {'f1' if not toggle else 'f2'}"

        idx_n += 1

    return True, None