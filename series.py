# Модуль для обчислення суми ряду
def calculate_series_sum(n):
    total_sum = 0.0
    for i in range(1, n + 1):
        total_sum += (i + 1) / i
    return total_sum
