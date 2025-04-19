# Empiric Prime Sieve

This repository presents an alternative approach to prime number identification based on cyclic frequency analysis, derived from empirical observations of the structure of numbers of the form \(6n \pm 1\).

## Description

The core idea of this model is that prime numbers greater than 3 can be detected through predictable patterns called **cyclic frequencies**, without relying on traditional factorization or prior knowledge of existing primes.

Unlike the Sieve of Eratosthenes or probabilistic tests, this method operates by observing arithmetic regularities within a sequence derived from simple operations. The result is a sieve-like mechanism that marks composite numbers through the detection of frequency-based collisions.

## Contents

- `empiric_sieve_validation.py`:  
  Python script to test the empirical sieve against SymPy’s standard list of primes, validating its consistency with known results up to a specified range.

- `Empiric_Prime_Sieve.pdf`:  
  Theoretical document (in English) detailing the foundations, logic, and structure of the proposed frequency-based sieve method.

## How to Use

Run the Python file using a standard Python interpreter. It will generate a list of prime numbers using the empirical sieve and compare it to the list provided by SymPy. Execution time and correctness are displayed at the end of the process.

## License

This project is released under a non-commercial license. For academic or research purposes only.

---

Author: Héctor Cárdenas Campos
