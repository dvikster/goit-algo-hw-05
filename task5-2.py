from typing import List, Tuple

def binary_search(arr: List[float], target: float) -> Tuple[int, float]:

    left, right = 0, len(arr) - 1
    iterations = 0  # Лічильник ітерацій
    upper_bound = None  # Верхня межа (найменший елемент, більший або рівний target)
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2  # Знаходимо середній індекс
        
        if arr[mid] == target:
            return iterations, arr[mid]  # Якщо знайдено точний збіг
        elif arr[mid] < target:
            left = mid + 1  # Продовжуємо пошук у правій половині
        else:
            upper_bound = arr[mid]  # Оновлюємо верхню межу
            right = mid - 1  # Продовжуємо пошук у лівій половині

    return iterations, upper_bound  # Якщо точного збігу немає, повертаємо верхню межу

# Відсортований список дробових чисел
sorted_array = [1.2, 2.4, 3.5, 4.8, 6.1, 7.3, 8.9]

# Тестові запити
print(binary_search(sorted_array, 3.5))  # Очікуваний результат: (ітерації, 3.5)
print(binary_search(sorted_array, 4.8))  # Очікуваний результат: (ітерації, 4.8)
print(binary_search(sorted_array, 7.0))  # Очікуваний результат: (ітерації, 7.3)
print(binary_search(sorted_array, 8.0))  # Очікуваний результат: (ітерації, 8.9)
