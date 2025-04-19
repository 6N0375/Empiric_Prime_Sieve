# Empiric Prime Sieve

This repository presents an alternative method to identify prime numbers based on empiric observation and cyclic frequency patterns.

## Overview

The model focuses on numbers of the form \(6n \pm 1\), using alternating cyclic frequency filters to predict and eliminate composite numbers. Unlike traditional sieves or probabilistic tests, this model does not rely on factorization or modular arithmetic.

## Contents

- `Empirical Cyclic Frequency Sieve.pdf`  
  A complete theoretical document (in English) that explains the mathematical foundation, logic, and structure of the proposed sieve.

- `Empiric_sieve_generator/empiric_frequency_sieve.py`  
  Python implementation of the sieve logic to generate and verify primes using cyclic frequencies.

- `Empiric_sieve_generator/verified_sieve_10M_validated.ipynb`  
  Jupyter notebook that validates the sieve’s results up to 10 million numbers.

- `Empiric_sieve_generator/verified_sieve_100M_validated.ipynb`  
  Jupyter notebook that validates the sieve’s results up to 100 million numbers.

## License

This project is licensed for **non-commercial and academic use only**.
