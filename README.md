# Empirical Prime Sieve

**Author:** Héctor Cárdenas Campos  
**License:** Non-commercial use only  

This repository contains an alternative method to detect prime numbers based on empirical observation. The model is centered on the sequence of numbers of the form 6n±1 and the use of cyclic frequency patterns to cancel out composite numbers.

---

## 📄 Documentation

- **Theoretical Foundation (English)**: [empiric_prime_sieve(en).pdf](./empiric_prime_sieve(en).pdf)  
  Full description of the frequency-based sieve, including the base sequence, generation of frequencies, and rules for primality evaluation without traditional factorization.

---

## 📁 Project Contents

```
empirical-prime-sieve/
│
├── empiric_prime_sieve(en).pdf          # Full theoretical document (English)
│
├── sieve_core.py                        # Generates 6n±1 base list and cancels composites via frequency patterns
├── sieve_predictive.py                  # Predicts primality by testing for collisions without generating lists
├── utils.py                             # Helper functions for modular structure
│
├── demo_sieve.ipynb                     # Jupyter demo: generation and visualization of cancelled numbers
├── demo_predictive.ipynb                # Jupyter demo: predictive primality test on large numbers
│
├── README.md                            # This file
```

---

## 🚀 How to Use

### Clone the repository
```bash
git clone https://github.com/your-username/empirical-prime-sieve.git
cd empirical-prime-sieve
```

### Run with Python
```bash
python sieve_core.py
```

### Open a notebook
Launch Jupyter and open one of the `.ipynb` demos to explore interactively.

---

## 🔎 Summary

- **Base sequence:** Only numbers of the form 6n±1 are considered.
- **Cyclic frequencies:** Composite numbers are cancelled using repeating patterns from smaller base primes.
- **Primality check:** A number is composite if any frequency pattern collides with it. One hit is enough.

This method avoids traditional factorization and aims for a predictive approach based on frequency logic.

---

## ⚠️ Limitations

- The model is empirical and under development.
- It may not detect all primes in all ranges compared to Eratosthenes.
- Optimizations and formal validation are in progress.

