# 🔍 Cyclic Frequency Sieve

An alternative method for identifying prime numbers, based on empirical observations of arithmetic patterns and cyclic frequencies in numbers of the form **6n ± 1**.

---

## 📌 Overview

This project proposes a sieve method to identify prime numbers greater than 3, using only modular arithmetic and pattern recognition. Unlike traditional methods such as the Sieve of Eratosthenes or probabilistic tests, this model works **without any factorization** and operates over a reduced search space.

---

## 🧠 Core Concept

All prime numbers greater than 3 belong to the sequence:

```
5, 7, 11, 13, 17, 19, 23, 25, 29, 31, ...
```

This corresponds to numbers of the form **6n ± 1**. These can be generated using an alternating pattern:

```text
Start at 5 → Add 2 → Add 4 → Add 2 → Add 4 → ...
```

Each number is assigned two frequencies derived from multiples of 4:

- **Frequency 2**: generated from 4n ± 1
- **Frequency 1**: Frequency 2 plus the 4n used

These frequencies form cyclic cancellation patterns across the list.

---

## 🔄 The Sieve Process

1. Generate the list of numbers in the form **6n ± 1**
2. Associate each with two frequencies (f₁, f₂)
3. Cancel numbers at positions defined by the alternating pattern:  
   `+f₁, +f₂, +f₁, +f₂, ...`
4. Repeat for each base number until its square is exceeded

Any number not cancelled by a frequency is retained as a prime.

---

## ⚙️ Python Implementation

This repository includes a Python version that:

- Generates the base sequence
- Computes frequency tables
- Applies the cancellation sieve
- Outputs prime numbers in the selected range

The code is **modular**, **transparent**, and easy to optimize.

---

## 📈 Performance

The sieve successfully identifies all primes in a given range using pure arithmetic logic. While not yet optimized for very large numbers like Mersenne primes, it demonstrates a promising structure for further development.

Earlier, lightweight versions (not included here) could evaluate some large primes quickly, but this current version prioritizes **strict adherence to the model**.

---

## 🧩 Opportunities for Improvement

- Precomputing and reusing frequency blocks
- Vectorization or parallel processing
- Heuristics to reduce the number of steps
- Formal mathematical analysis of its periodic structure

---

## 👨‍💻 Author

**Héctor Cárdenas Campos**  
Email: hectorcardc@gmail.com  
License: Non-commercial use only

---

## 📚 Description

Alternative method to identify prime numbers based on empirical observation and cyclic frequency cancellation patterns in the sequence **6n ± 1**.
