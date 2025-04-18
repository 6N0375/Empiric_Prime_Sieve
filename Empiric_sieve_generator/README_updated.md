# Empirical Frequency Sieve

This repository contains an alternative method to identify prime numbers based on empiric observation and cyclic frequency patterns.

## Overview

The model focuses on numbers of the form `6n ± 1`, using alternating cyclic frequency filters to predict and eliminate composite numbers.
Unlike traditional sieves or probabilistic tests, this model does not rely on factorization or modular arithmetic.

## Structure

- `empiric_frequency_sieve.py` — Contains the core function to generate primes using the empirical sieve.
- `verified_sieve_100M_validated.ipynb` — Full validation up to 100 million, includes timing and comparison with sympy.
- `verified_sieve_10M_validated.ipynb` — Lighter version for quicker testing up to 10 million, also includes validation.

## How to Use

1. Upload `empiric_frequency_sieve.py` in Colab when prompted.
2. Run all cells in either notebook.
3. Observe execution time and prime count.
4. Review the validation output to confirm exactness.

## Performance Benchmarks

### 100 Million Range

- **Execution time:** 105.13 seconds
- **Primes found:** 5,761,455
- **First 10 primes generated:** [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
- **Validation:** Passed (exact match with sympy)

### 10 Million Range

- **Execution time:** ~9 seconds (may vary)
- **Primes found:** 664,579
- **Validation:** Passed (exact match with sympy)

These results confirm that the sieve is capable of large-scale prime detection with high accuracy and efficiency, relying solely on pattern-based elimination without classical factorization techniques.

## License

Author: Hector Cárdenas Campos  
License: Non-commercial use only
