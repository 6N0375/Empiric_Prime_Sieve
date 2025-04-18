# Empiric Prime Project

**Author:** Héctor Cárdenas Campos  
**Email:** hectorcardc@gmail.com  
**License:** Non-commercial use only

This project presents an alternative model for identifying prime numbers using empirically observed cyclic frequency patterns, focused on numbers of the form 6n±1. The approach includes:

- A **frequency-based sieve** for generating verified prime lists.
- A **predictive primality checker** that determines whether a number is prime without generating any list.
- Verification tools that compare results with classical methods such as `sympy`.

---

## 📁 Project Structure

```
empiric_prime_project/
├── empiric_sieve_generator/
│   ├── empiric_frequency_sieve.py
│   ├── verified_sieve.ipynb
│   └── README.md
│
└── empiric_predictive_checker/
    ├── predictive_primality.py
    ├── predictive_checker.ipynb
    └── README.md
```

Each folder contains:
- A Python module (`.py`) with the main algorithm.
- A Colab-ready notebook (`.ipynb`) demonstrating its functionality.
- A local `README.md` with usage instructions.

---

## ⚙️ Requirements

The notebooks depend on:

- Python 3.x
- `sympy` (for result verification in the sieve module)

> You can run the notebooks directly in [Google Colab](https://colab.research.google.com) by uploading the required `.py` file when prompted.

---

## ✅ Validation

The empiric sieve has been verified against official prime lists (e.g., via `sympy`) and has shown consistent accuracy up to significant bounds (e.g., 10,000).

---

## 📜 License

This project is licensed for **non-commercial use only**.
