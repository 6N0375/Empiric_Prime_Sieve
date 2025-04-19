def check_primality_by_frequencies(X, extra=1000):
    from math import isqrt

    def f1(a): return 2 * a + 3
    def f2(a): return (2 * a + 3) * 2 + (-1)**a
    def f3(a): return (6 * a + 9 + (-1)**a) // 2

    if X <= 3:
        return "prime" if X in (2, 3) else "composite"
    if X % 2 == 0 or X % 3 == 0:
        return "composite"
    if X % 6 not in (1, 5):
        return "outside domain"

    a_min = (isqrt(X) + 5) // 6
    for a in range(a_min + extra):
        base = f3(a)
        if base >= X:
            break
        f = f1(a) + f2(a)
        offset = f1(a) + a
        if (X - offset) % f == 0:
            return "composite"
    return "prime"
