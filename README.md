# 🔍 Empiric Prime Sieve

**Alternative method to identify prime numbers using cyclic frequency cancellation, based solely on arithmetic structure and without factorization.**

![Prime Distribution Illustration](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Prime_number_theorem.svg/640px-Prime_number_theorem.svg.png)

---

## 📘 Summary

This project introduces an alternative to the Sieve of Eratosthenes, grounded in **empirical observations** of arithmetic regularities. It uses a cyclic mechanism to eliminate composite numbers from the sequence \(6n \pm 1\), which includes all primes greater than 3.

> 🚫 No divisions  
> 🚫 No modulos  
> ✅ Only structured frequency patterns

---

## 🧩 Core Concepts

### 🔢 Base Sequence: \(6n \pm 1\)

Only numbers of the form:

```
6n + 1   and   6n - 1 = 6n + 5
```

can be prime when \(n > 0\). The algorithm generates the sequence:

```
5, 7, 11, 13, 17, 19, 23, 25, 29, 31, ...
```

This sequence includes both primes and composites.

---

### ♻️ Frequency System

Each number in the base list is assigned two **frequencies**, derived from multiples of 4:

- **Frequency 2**: \(f_2 = 4n \pm 1\)
- **Frequency 1**: \(f_1 = f_2 + 4n\)

They are applied in a cyclic pattern:

```
f₁, f₂, f₁, f₂, ...
```

to cancel composite numbers in the sequence.

---

## ⚙️ Python Implementation

### 📂 Features

- 🔸 **Generates** the base list of \(6n \pm 1\) numbers.
- 🔸 **Assigns** and stores the corresponding frequencies.
- 🔸 **Eliminates** composites through cyclic application of frequencies.
- 🔸 **Exports** the list of confirmed primes greater than 3.

### ❗ Important Note

This version does **not include** individual primality checks or prediction modules.  
The focus is strictly on **list-based sieving** through structured cyclic patterns.

---

## 📈 Performance

- ✅ Capable of generating lists up to **10 million primes** in ~10 seconds (tested).
- ✅ Fully aligned with the arithmetic model—no shortcuts, approximations, or randomness.
- ⚠️ Not yet optimized for memory or parallelization.

---

## ⚠️ Limitations

- 🚫 Does not include primes < 5 (i.e., 2 and 3 must be added manually).
- 🧭 Works **only** over the domain \(6n \pm 1\).
- 📐 Lacks a formal mathematical proof (empirically validated, structurally coherent).
- 🐌 Performance over extremely large ranges is limited in current state.

---

## 🔮 Future Improvements

- 🔁 Reuse and precompute frequency blocks for faster sieving.
- 🧵 Parallel processing of cyclic cancellations.
- 💡 Vectorization and memory-efficient structures.
- 📚 Mathematical formalization of the cyclic behavior.

---

## 👤 Author

**Héctor Cárdenas Campos**  
📧 [hectorcardc@gmail.com](mailto:hectorcardc@gmail.com)  
🛡️ License: Non-commercial use only.

---

## 🧠 Explore the Theory

If you're interested in the full theoretical documentation of the sieve model, including equations, cyclic patterns, and observations about pattern reuse, see the accompanying LaTeX document or published version.
