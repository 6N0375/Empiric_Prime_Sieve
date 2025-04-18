"""
Predictive Primality Checker
----------------------------
Given a number T, this function determines whether T is prime according to the 
frequency sieve model. It simulates the alternation of step patterns F1 and F2 
starting from each base A(n) until a collision (i.e., exact match) with T 
indicates that T is composite.
"""


from math import isqrt

def es_primo_por_frecuencias_corr(T):
    """
    Evalúa si T es primo según el modelo de criba por frecuencias.
    Sigue la lógica exacta de la macro: desde cada base, se alterna entre F1 y F2 como pasos.
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

        # Simular la pista desde la posición del número base
        pos = base
        toggle = True
        while pos < T:
            paso = f1 if toggle else f2
            pos += paso
            toggle = not toggle

        if pos == T:
            return False, f"colisión por base {base} con paso {'f1' if not toggle else 'f2'}"

        idx_n += 1

    return True, None
