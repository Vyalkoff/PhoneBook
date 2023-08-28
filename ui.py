class UserInterface:
    """
    Класс для методов интерфейса
    """

    @staticmethod
    def show_menu():
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Поиск записи')
        print('3. Редактировать запись')
        print('0. Закрыть программу.\n')

    @staticmethod
    def show_menu_two(headers):
        """

        :param headers: Заголовки
        :return: Выводит заголовки (ключ, значение)
        """
        print('Выберите по какому параметру или запишите через ","  для выбора нескольких параметров:')
        for key, name in headers.items():
            print(f'{key}. {name}.')

    @staticmethod
    def show_menu_three():
        print('1. Добавить новую запись.')
        print('2. Изменить существующую запись.')
        print('3. Удалить запись.')
        print('4. Назад')

    @staticmethod
    def show_menu_fake():
        print('1. Заполнить справочник тестовыми данными ')
        print('0. Нет')


class UserExperience:
    """
    Класс для взаимодействия пользователя с программой
    """

    @staticmethod
    def success():
        print('-' * 5, 'Успех', '-' * 5)

    @staticmethod
    def show_menu_create(headers):
        """

        :param headers:Заголовки
        :return: Возвращает список введенных значения для записи
        """
        value = [input(f'Введите {name}: ') for name in headers.values()]
        return value

    @staticmethod
    def show_and_get_value(headers, number_search_param):
        value = []
        for name in number_search_param:
            value.append(f"{headers[int(name)]} == '{input(f'Введите {headers[int(name)]}: ').replace(' ', '_')}'")

        str_search = ' & '.join(value)

        return str_search

    @staticmethod
    def choice_menu():
        return int(input('Выберите пункт меню: '))

    @staticmethod
    def get_param_for_update():
        change_param = input('Введите старые данные: ')
        update_param = input('Введите новые данные: ')
        return change_param, update_param

    @staticmethod
    def get_number_input():
        try:
            return int(input('Введите количество записей на странице: '))
        except ValueError as er:
            print(er, 'Только цифры')

    @staticmethod
    def enter_parameters():
        return input('Ввести параметры: ').split(',')

    @staticmethod
    def get_id_for_delete_or_update():
        return int(input('Введите id: '))
