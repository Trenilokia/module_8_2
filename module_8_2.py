def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    if not isinstance(numbers, int):
        for number in numbers:
            try:
                result += int(number)
            except ValueError:
                incorrect_data += 1
            except TypeError:
                incorrect_data += 1
        return result, incorrect_data
    else:
        return None, incorrect_data

def calculate_average(numbers):
    total_numbers = 0
    sum_numbers = personal_sum(numbers)[0]
    try:
        for number in numbers:
            if not isinstance(number, int):
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
            else:
                total_numbers += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
    try:
        return sum_numbers / total_numbers
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

