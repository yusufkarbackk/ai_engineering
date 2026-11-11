from data_utils import calculate_average, find_max, find_min


def analyze_data(numbers):
    result = {}

    if len(numbers) < 1:
        raise ValueError("numbers kosong")

    average = calculate_average(numbers)
    maximum = find_max(numbers)
    minimum = find_min(numbers)

    result["average"] = average
    result["maximum"] = maximum
    result["minimum"] = minimum
    return result


if __name__ == "__main__":
    print(analyze_data([10, 20, 30, 40, 50]))
# analyze_data([10, 20, 30, 40, 50])
