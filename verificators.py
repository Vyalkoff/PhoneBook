def is_accessible(path):
    """
    Проверка, является ли файл или папка из `path`
    доступным для работы.

    :param path : Путь к файлу
    :return: Bool
    """

    try:
        file = open(path)
        file.close()
    except IOError:
        return False
    return True


def more_zero(value):
    """
    :param value: число
    :return:  False если меньше 1
    """
    try:
        if value >= 1:
            return True
    except TypeError as ter:
        print(ter, 'Только число')


def in_data(value):
    """

    :param value: Dataframe
    :return:  Возвращает Dataframe если не пустой
    """
    if value.empty:
        return 'Такие данные не найдены'
    else:
        return value
