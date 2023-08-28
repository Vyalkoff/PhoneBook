from mimesis import Generic
from mimesis.locales import Locale
from mimesis.builtins import RussiaSpecProvider


def fake_value():
    fake = Generic(locale=Locale.RU)
    fake.add_provider(RussiaSpecProvider)
    row = [[
        fake.person.first_name(),
        fake.person.last_name(),
        fake.russia_provider.patronymic(),
        fake.finance.company(),
        fake.person.phone_number(),
        fake.person.phone_number()]
        for _ in range(100)]

    # Генерируем строки

    return row
