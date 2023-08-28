import pandas as pd
from ui import UserInterface, UserExperience
import verificators as vrf


class CRUD:
    """
    Класс для чтения, создания,удаления,обновления
    """

    def __init__(self):

        self.ui = UserInterface()
        self.ue = UserExperience()

    @staticmethod
    def read(path, count_page=10, flag=False, search=False):
        """

        :param search: флаг для поиска
        :param path: Название файла
        :param count_page:  Количество строк на странице
        :param flag: По умолчанию для чтения
        :return: Вывод файла в командной строке(по умолчанию)

        """
        if search:
            return pd.read_csv(path)

        if vrf.more_zero(count_page):
            all_file = pd.read_csv(path, chunksize=count_page)

            if flag:
                for page in all_file:
                    print(page)

        else:
            print("Не может быть меньше 1")

    def search(self, path, headers, number_search_param):
        """


        :param path: Путь файла
        :param headers: Заголовки файла
        :param number_search_param: Номер заголовка для поиска
        :return: Возвращает, искомые данные
        """

        str_search = self.ue.show_and_get_value(headers, number_search_param)

        file_frame = self.read(path, search=True)

        return vrf.in_data(file_frame.query(str_search))

    def update(self, path, headers, value_id):
        """

        :param value_id:
        :param headers: Заголовки
        :param path: Путь файла
        :return: Файл и измененными данными
        """
        frame_file = self.read(path=path, search=True)
        update_row = frame_file.loc[[value_id]]  # Строка по id
        data_update_list = update_row.values[0].tolist()  # Перевод в список
        print(update_row)

        update_param = self.ue.get_param_for_update()  # Данные для замены
        id_old_param = data_update_list.index(update_param[0])  # id изменяемого
        data_update_list.pop(id_old_param)  # Удалить старую информацию
        data_update_list.insert(id_old_param, update_param[1])  # Заменить старый на новый по id
        print(data_update_list)
        frame_file.loc[value_id] = data_update_list  # Обновить Frame
        frame_file.to_csv(path, index=False)  # Записать в файл

    def create(self, path, headers, value=None, test=False):
        """
        :param headers: Заголовки
        :param test: Доступ для до записи файла(по умолчанию)
        :param path: Путь файла
        :param value: список записей
        :return: Добавляет запись в справочник
        """
        if test:
            file = pd.DataFrame(columns=headers, data=value)
            file.to_csv(path, index_label='id')
        else:
            old_frame = self.read(path, search=True)
            value.insert(0, len(old_frame.index))
            old_frame.loc[len(old_frame.index)] = value
            old_frame.to_csv(path, index=False)

    def delete(self, path, headers, value_id):

        df = self.read(path, headers, search=True)
        df.drop(index=value_id)
        df.to_csv(path, headers)
