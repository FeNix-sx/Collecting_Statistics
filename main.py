import time
import base64

from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from mytools import ColorPrint
from mytools import statistic
from mytools import WorkingYandexDisk
from mytools import delay_print

printer = ColorPrint().print_error
printinf = ColorPrint().print_info
printw = ColorPrint().print_warning
printy = ColorPrint().print_yellow

PROGRAM = "COLLSTAT"
VERSION = "version_v_1.9 (02.05.2025) for Win 7,10"


def upload_to_yadick(content: dict)->None:
    """
    Загружает на яндекс диск в папку folder_name(ip-адрес пользователя)
    статистику по работе программы:
    :param folder_name: IP-адрес пользователя
    :return:
    """
    # загрузка параметров: FOLDER_PATH - папка, в которую сохранится folder_name на яддекс_диске
    # YANDEX_TOKEN - токен яндекс REST API
    try:
        YANDEX_TOKEN = 'y0__xDxk5QJGP3cJCDnjcT_Ek1FhLPp6FOnMXL3ClW-PSrcDxGd'

        if YANDEX_TOKEN == "":
            raise ValueError

    except Exception as ex:
        print(ex)

    try:
        folder_name = content['IP']
        yadisk = WorkingYandexDisk(yandex_token=YANDEX_TOKEN)

        # имя файла, равно текущему времени на ПК
        now = datetime.now()
        content['time_start'] = f'{now.strftime("%Y.%m.%d_%H:%M:%S")}'
        filename = f'{now.strftime("%Y.%m.%d_%H.%M.%S")}.txt'

        # Конвертация словаря в строку и кодирование в base64
        encoded_str = base64.b64encode(str(content).encode()).decode()

        # Создание BytesIO объекта с содержимым файла в формате base64
        file_contents = BytesIO(encoded_str.encode())

        yadisk.upload_of_yd(
            filename=filename,
            folder_name=folder_name,
            file_obj=file_contents
        )

    except Exception as ex:
        printer(ex)


def main_func()->None:
    statistic.get_version(program=PROGRAM, version=VERSION)
    content = statistic.get_full_info
    upload_to_yadick(content)


def main_multiprocessing():
    text = [
        VERSION,
        "Программа собирает информацию об интернет соединении",
        "Благодарю за использование программы!"
    ]
    for item in text:
        delay_print(
            text=item,
            func=printw,
            sleep_time= 0.015
        )
    # Создаем экземпляр ThreadPoolExecutor с двумя потоками
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Запускаем функции statistic.draw и main_func в фоновом режиме
        future1 = executor.submit(statistic.draw)
        future2 = executor.submit(main_func)

        # Ожидаем завершение обоих функций
        future1.result()
        future2.result()


if __name__ == '__main__':
    main_multiprocessing()
    delay_print(
        text='Каждый запуск помогает мне в обучении',
        func=printw,
        sleep_time=0.015
    )
    statistic.print_smile()
    time.sleep(3)

    # pip freeze > requirements.txt
    # pip install -r requirements.txt