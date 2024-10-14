"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    number_list = list(range(1,101))
    count_list = []
    
    def halved_predict(number_list, count):
        count +=1
        if number != number_list[0] and number != number_list[-1]:
            ind = len(number_list)//2
            predict_number = number_list[ind]
            if number== predict_number:
                count_list.append(count)
            elif number < predict_number:
                number_list = number_list[1:ind]
                halved_predict(number_list, count)
            else:
                ind += 1
                number_list = number_list[ind:-1]
                halved_predict(number_list, count)
        elif number == number_list[0]:
            count_list.append(count)
        else:
            count_list.append(count)
        return count_list[0]
    result = halved_predict(number_list, count)
    return result

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)