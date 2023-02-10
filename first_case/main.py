# 1. Какие шаги ты бе предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?
'''В случае, если пользователь сообщает об ошибке 500 (Internal Server Error), я бы выполнил следующие шаги:
Подтвердить симптомы: Убедился бы, что пользователь действительно получает ответ с кодом 500.
Исследовать логи: Проверил бы  логи сервера, чтобы узнать, что именно вызывает ошибку. Это может помочь понять, в чем проблема.
После чего, можно было бы судить в чем проблемма данной ошибки  и приступать к ее решению.
'''
# 2.
from typing import Callable, List


def create_handlers(callback: Callable[[int], None]) -> List[Callable[[], None]]:
    handlers = []
    for step in range(5):
        handlers.append(lambda step=step: callback(step))
    return handlers


def execute_handlers(handlers: List[Callable[[], None]]):
    for handler in handlers:
        handler()


# 3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них содержит атрибуты?
import requests
from bs4 import BeautifulSoup

url = "https://greenatom.ru/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tag_count = 0
attribute_count = 0

for tag in soup.find_all(True):
    tag_count += 1
    if tag.attrs:
        attribute_count += 1

print("Number of HTML tags:", tag_count)
print("Number of HTML tags with attributes:", attribute_count)


# 4. Функция возвращающая IP-адрес компьтера
def get_ip_address():
    response = requests.get("https://ifconfig.me/")
    return response.text.strip()


print(get_ip_address())


# 5. Сравнение версий
def compare_versions(version_a, version_b):
    version_a_list = version_a.split(".")
    version_b_list = version_b.split(".")

    for i in range(max(len(version_a_list), len(version_b_list))):
        a = int(version_a_list[i]) if i < len(version_a_list) else 0
        b = int(version_b_list[i]) if i < len(version_b_list) else 0

        if a < b:
            return -1
        elif a > b:
            return 1

    return 0


print(compare_versions('1.1', '1.10'))
