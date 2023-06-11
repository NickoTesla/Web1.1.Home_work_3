from multiprocessing import Pool, cpu_count


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results


# Приклад використання
if name == 'main':
    numbers = [128, 255, 99999, 10651060]

    # Синхронна версія
    results_sync = [factorize(number) for number in numbers]
    print("Синхронна версія:")
    for number, result in zip(numbers, results_sync):
        print(f"Число {number}: {result}")

    # Паралельна версія
    results_parallel = factorize_parallel(numbers)
    print("Паралельна версія:")
    for number, result in zip(numbers, results_parallel):
        print(f"Число {number}: {result}")
