def find_outlier(integer):
    even_numbers = [number for number in integer if number % 2 == 0]
    odd_numbers = [number for number in integer if number % 2 != 0]

    if len(even_numbers) == 1:
        return even_numbers[0]
    else:
        return odd_numbers[0]
