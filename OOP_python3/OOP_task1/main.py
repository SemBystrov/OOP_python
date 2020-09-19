"""
Лабораторная работа №1. Знакомство с python
Выполнил: Быстров Семён, группа К33202
"""

from typing import List


def process_numbers(numbers: List[float]) -> List[float]:
    """
    Функция, которая выполняет специфическую задачу из задания:
    умножение на 0.13 и округление элементов, сортировка массива

    Вынес в одну функцию, так как каждое действие
    пишется в одну строчку и разбивать на отдельные функции
    не имеет смысла

    :param numbers: Массив чисел
    :returns: Обработанный массив
    """
    return sorted([round(number * 0.13, 2) for number in numbers])


def save_numbers_to_file(numbers: List[float], name: str) -> None:
    """
    Процедура, сохраняющая массив чисел в файл name.list

    :param numbers: Массив для сохранения
    :param name: Название файла
    """
    to_file = open(name + ".list", "w")
    to_file.write(", ".join(map(str, numbers)))
    to_file.close()


def ask_user(question: str) -> bool:
    """
    Задаёт вопрос пользователю в консоли

    :return: Ответ пользователя
    """
    ans_dict: dict = {"Y": True, "N": False}
    ans: str = input(question + " (Y/N): ")
    return ans_dict.get(ans, False)


if __name__ == '__main__':

    continue_program: bool = True  # флаг для выполнения программы

    while continue_program:
        numbers: List[float] = []
        # Вводим массив
        print("Введите массив:")
        try:
            numbers = list(map(float, input().split(",")))
        except:
            continue_program = ask_user("Неверный формат ввода.\nНачать выполнение снова?")
            continue
        # Обрабатываем массив
        processed_numbers = process_numbers(numbers)
        # Печать элементов
        print(*processed_numbers)
        # Сохранение массива
        if ask_user("Сохранить массив?"):
            fname: str = input("Введите имя файла: ")
            save_numbers_to_file(processed_numbers, fname)

        continue_program = ask_user("Попробовать ещё?")
