# Frequency-Based Prime Sieve

This repository presents an alternative method to identify prime numbers based on an empirical frequency model. The model leverages the 6n±1 structure and simulates predictable cancellation patterns (frequencies) to sieve out composite numbers without traditional factorization.

---

## 📁 Contents

### `frequency_sieve_full.py`
A complete implementation of the frequency-based prime sieve, composed of two main components:

- **`criba_frecuencias_excel_style_opt(limite, max_producto=10**6)`**  
  Generates a list of prime numbers up to `limite` using a frequency sieve. Applies alternating frequency steps (F1, F2) starting from base numbers of the form A(n) = (6n+9+(-1)^n)//2.

- **`es_primo_por_frecuencias_corr(T)`**  
  Checks whether a number `T` is prime based on predictive collision with a frequency pattern. If a base's frequency steps land exactly on `T`, it is marked as composite.

---

### `predictive_primality.py`
A standalone version of the primality checker using the same predictive mechanism. Useful for individual number analysis without generating full lists.

---

## 🔍 How It Works

This model is rooted in the following principles:

1. **Candidate Numbers**  
   Only numbers of the form 6n±1 are considered as potential primes.

2. **Frequencies**  
   For each base `A(n)`, two frequency steps are used:
   - F1(n) = 2*(2n+3) + (-1)^n
   - F2(n) = 2n + 3

3. **Collision Detection**  
   A number is considered **composite** if any simulated frequency path from a base lands exactly on it. If no such collision occurs up to √T, it is **prime**.

---

## 📜 License

Author: Héctor Cárdenas Campos  
License: Non-commercial, research and academic use only.
