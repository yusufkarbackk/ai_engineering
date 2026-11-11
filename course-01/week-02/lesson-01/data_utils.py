def calculate_average(numbers):
    if len(numbers) < 1:
        raise ValueError("numbers kosong")
    return sum(numbers) / len(numbers)


def find_max(numbers):
    if len(numbers) < 1:
        raise ValueError("numbers kosong")
    return max(numbers)


def find_min(numbers):
    if len(numbers) < 1:
        raise ValueError("numbers kosong")
    return min(numbers)
