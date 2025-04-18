# Empirical Frequency-Based Prime Sieve

**Author:** Héctor Cárdenas Campos  
**License:** Non-commercial use only

This repository presents an alternative model for identifying prime numbers using cyclic frequency patterns, based on numbers of the form 6n±1. The method includes:

- A **frequency-based sieve** for generating prime lists
- A **predictive primality checker** that works without generating any list
- Verification tools to compare results with classical methods (like `sympy`)

---

## 📂 Project Structure

```
frequency_sieve_package/
├── predictive_checker/
│   ├── predictive_primality_en.py
│   ├── predictive_checker_colab_en.ipynb
│   └── README.md
│
└── prime_sieve_verification/
    ├── frequency_sieve_full_en.py
    ├── verified_sieve_colab_en.ipynb
    └── README.md
```

Each folder contains:
- A Python module (`.py`) with the core logic
- A Colab-ready notebook (`.ipynb`) that demonstrates its use
- A local README with usage instructions

---

## 🔧 Requirements

The notebooks depend on:

- Python 3.x
- `sympy` (for verification in `prime_sieve_verification`)

> These can be used directly in [Google Colab](https://colab.research.google.com) by uploading the required `.py` file when prompted.

---

## ✅ Validation

The frequency-based sieve has been validated against official prime lists (e.g., via `sympy`) and passes all correctness tests up to large bounds (e.g., 10,000).

---

## 📜 License

This project is licensed for **non-commercial use only**.

