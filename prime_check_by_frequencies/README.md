from prime_check_verified_v2 import check_primality

check_primality(89)          # → 'prime'
check_primality(2229)        # → 'composite'
check_primality(2**127 - 1)  # → 'prime'
check_primality(2**12800 - 1)  # → 'unknown'
