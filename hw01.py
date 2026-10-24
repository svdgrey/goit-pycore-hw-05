
def caching_fibonacci():
    # Cache previously calculated Fibonacci numbers.
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Example usage:
def main():
    fib = caching_fibonacci()
    print(fib(10))  # 55
    print(fib(15))  # 610

if __name__ == "__main__":
    main()
