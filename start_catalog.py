from main import Main

FILENAME = "Phone_book_ENG.csv"
HEADERS = ['имя', 'фамилия', 'отчество', 'название организации', 'телефон рабочий', 'телефон личный (сотовый)']

if __name__ == '__main__':
    Main(FILENAME, HEADERS).start()
