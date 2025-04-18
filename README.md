# Empirical Prime Sieve Project

This repository presents a complete theoretical and practical exploration of a novel method to identify prime numbers based on cyclic frequency patterns derived from the 6n ± 1 number form.

## Repository Contents

- 📄 `empiric_prime_sieve.pdf`  
  A comprehensive theoretical document detailing the foundations of the frequency-based sieve model, including its mathematical basis, structure, and implications. This serves as the core explanation of the model.

- 📁 `prime_sieve/`  
  This folder contains the implementation of the sieve in Python and two Jupyter notebooks:
  
  - `verified_sieve_100M_validated.ipynb`: Performs the sieve up to 100 million and validates the results.
  - `verified_sieve_10M_validated.ipynb`: A lightweight version up to 10 million for quick testing.
  - `empiric_frequency_sieve.py`: The Python module implementing the model.

- 📁 `empiric_predictive_checker/`  
  This submodule explores a predictive approach to primality based on pattern collisions. It attempts to verify the primality of an individual number without generating full lists, using cyclical frequencies and a bounded window derived from the square of the candidate number.

## Highlights

- ✅ Completely original approach not based on traditional factorization or probabilistic methods.
- 🔁 Uses predictable cyclic patterns for elimination based on empirical observation.
- 🔬 Fully validated up to 100 million primes using standard libraries such as `sympy`.
- 📈 Performance demonstrated through benchmark notebooks.
- 🧠 Includes a predictive primality checker that leverages cyclical structure and frequency overlap.

## How to Get Started

1. Review the theoretical model in `empiric_prime_sieve.pdf`.
2. Use the notebooks in `prime_sieve/` to test and explore the implementation.
3. Explore the predictive module in `empiric_predictive_checker/` for individual primality analysis.
4. Upload the required Python files when prompted in the notebooks (e.g. in Google Colab).

## License

Author: Hector Cárdenas Campos  
License: Non-commercial use only
