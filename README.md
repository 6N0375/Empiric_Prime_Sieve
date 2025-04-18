# Empiric Prime Sieve

**Alternative method to identify prime numbers based on cyclic frequency cancellation.**

## Overview

This project presents an alternative sieve for prime detection, derived from empirical observation of arithmetic patterns. It focuses exclusively on numbers of the form \(6n \pm 1\), exploiting their internal modular properties to build a list of primes greater than 3.

The model uses a system of **cyclic frequencies** that systematically eliminate composites without the need for factorization or divisibility checks.

## Key Concepts

- **Base Sequence**: All primes greater than 3 appear within the sequence \(6n \pm 1\).
- **Frequency Pattern**: Each number in this sequence is associated with two frequencies derived from modified multiples of 4. These frequencies are applied in an alternating manner to eliminate composites.
- **Structured Cancellation**: The algorithm applies these frequencies in predictable, repeating cycles, enabling the detection of primes through cancellation alone.

## Python Implementation

The implementation is written in Python and focuses exclusively on:

- Generating a base list of numbers of the form \(6n \pm 1\).
- Associating each number with its corresponding frequencies.
- Applying the cancellation pattern to identify and remove composite numbers.

⚠️ The current version does **not** perform individual primality testing for arbitrary numbers. The project focuses on list generation through the sieve mechanism.

## Performance

- Efficient for generating lists up to several million entries.
- Fully adheres to the theoretical structure of the cyclic sieve.
- No factorization or modulo operations involved in the cancellation process.

## Limitations

- Does not cover primes < 5 (these must be verified separately).
- Applies only to the subset \(6n \pm 1\).
- Formal mathematical proof is still under development.
- Performance over extremely large ranges is currently limited by lack of optimization.

## Future Work

- Optimize frequency storage and reuse.
- Implement parallel processing for large-scale ranges.
- Explore vectorized applications of cancellation blocks.
- Formalize theoretical foundations.

## License

Non-commercial use only.  
Author: Héctor Cárdenas Campos
