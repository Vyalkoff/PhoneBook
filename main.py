from ui import UserInterface, UserExperience
from verificators import is_accessible
from crud import CRUD
from fake_generate_csv import fake_value


class InitCatalog:

    def __init__(self, path, headers):
        """

        :param path: Название файла
        :param headers: Заголовки справочника
        """

        self.path = path
        self.headers = [title.replace(' ', '_') for title in headers]
        # Создается файл с заголовками
        if not is_accessible(self.path):
            UserInterface().show_menu_fake()
            if UserExperience().choice_menu() == 1:
                CRUD().create(path=self.path, headers=self.headers, value=fake_value(), test=True)

            # Выбор для заполнения тестовыми данными

            UserExperience().success()

            print(f'Файл {self.path} создан')

    def get_path(self):
        """

        :return: Возвращает название файла
        """
        return self.path

    def dict_headers(self):
        """

        :return: Возвращает словарь заголовков под нумерацией
        """
        return {i[0]: i[1] for i in enumerate(self.headers, start=1)}


class Main(InitCatalog):
    """
    Главный класс для работы справочника
    """

    def __init__(self, path, headers):
        super().__init__(path, headers)

        self.ui = UserInterface()
        self.ue = UserExperience()
        self.path = self.get_path()
        self.headers = self.dict_headers()
        self.crud = CRUD()

    def start(self):

        while True:

            self.ui.show_menu()  # Вывести меню
            number_input = self.ue.choice_menu()  # Получить ответ

            if number_input == 0:
                break

            elif number_input == 1:

                count_number_page = self.ue.get_number_input()
                self.crud.read(self.path, count_number_page, flag=True)

            elif number_input == 2:
                self.ui.show_menu_two(self.headers)
                list_number_value = self.ue.enter_parameters()
                result_find = self.crud.search(self.path, self.headers, list_number_value)
                print(result_find)
                break

            elif number_input == 3:
                self.ui.show_menu_three()
                number_crud_param = self.ue.choice_menu()
                if number_crud_param == 1:
                    value = self.ue.show_menu_create(self.headers)

                    self.crud.create(self.path, self.headers, value)

                    self.ue.success()
                elif number_crud_param == 2:
                    value_id = self.ue.get_id_for_delete_or_update()
                    self.crud.update(self.path, self.headers, value_id)
                    self.ue.success()
                elif number_crud_param == 3:

                    value_id = self.ue.get_id_for_delete_or_update()
                    self.crud.delete(self.path, self.headers, value_id)
                    self.ue.success()
                elif number_crud_param == 4:
                    continue
            else:
                continue
