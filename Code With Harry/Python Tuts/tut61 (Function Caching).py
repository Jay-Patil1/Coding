# FUNCTION CACHING
import time
from functools import lru_cache  # lru_cache is a decorator.


@ lru_cache(maxsize=3)  # The last () values are stored.
def some_work(n):
    # Some task taking n seconds.
    time.sleep(n)  # The time required to complete the function.
    return n


if __name__ == '__main__':
    print("Now running some_work.")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done.. Calling again")
    input()
    some_work(3)  # This takes time as some_work(3) was not stored.
    # To avoid this we can increase the maxsize value.
    print("Called again.")

# TASK
# Asks for how many values to cache.
# Give it to lru cache.
