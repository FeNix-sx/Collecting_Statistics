import json
import base64

from io import BytesIO
from zipfile import ZipFile
from mytools import YaDisk, WorkingYandexDisk

def test():
    dict_info = {'COLLSTAT': 'version_v_1.7.1 (09.09.23) for Win 7,10', 'IP': '109.252.8.126', 'Prov': 'Moscow Local Telephone Network (OAO MGTS)', 'Org': 'OAO Mgts)', 'Country': 'Russia', 'regionName': 'Moscow', 'lat': 55.7483, 'lon': 37.6171, 'OS': {'os_name': 'Windows', 'os_version': '10', 'os_architecture': 'AMD64'}, 'CPU': {'name': 'Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz', 'model': 'Intel64 Family 6 Model 158 Stepping 12, GenuineIntel', 'physical_cores': 8, 'logical_cores': 8, 'min frequency': 0.0, 'max frequency': 3600.0, 'current frequency': 3600.0}, 'MB': {'Name:': 'ASUSTeK COMPUTER INC.', 'Model:': 'ROG STRIX Z370-H GAMING', 'Chipset:': 'Основная плата'}, 'RAM': {'RAM_modules': 4, 'BANK 0': {'manufacturer': 'Kingston', 'model': 'KF426C16BB1K2/32    ', 'capacity': '16.0GB', 'speed': 2667}, 'BANK 1': {'manufacturer': 'Kingston', 'model': 'KF426C16BB1K2/32    ', 'capacity': '16.0GB', 'speed': 2667}, 'BANK 2': {'manufacturer': 'Kingston', 'model': 'KHX2666C16/16G      ', 'capacity': '16.0GB', 'speed': 2667}, 'BANK 3': {'manufacturer': 'Kingston', 'model': 'KF426C16BB1K2/32    ', 'capacity': '16.0GB', 'speed': 2667}}, 'GPU': {'VideoController1': {'manufacturer': 'NVIDIA', 'model': 'NVIDIA GeForce RTX 2070'}}, 'HDD physical': {'Samsung SSD 970 EVO 250GB': {'model': 'Samsung SSD 970 EVO 250GB', 'manufacturer': '', 'total_size': '232.88GB', 'interface': 'SCSI'}, 'Hitachi HDS722020ALA330': {'model': 'Hitachi HDS722020ALA330', 'manufacturer': '', 'total_size': '1863.01GB', 'interface': 'SCSI'}, 'ADATA SX6000LNP': {'model': 'ADATA SX6000LNP', 'manufacturer': '', 'total_size': '953.86GB', 'interface': 'SCSI'}, 'OCZ-VERTEX2 3.5': {'model': 'OCZ-VERTEX2 3.5', 'manufacturer': '', 'total_size': '111.79GB', 'interface': 'SCSI'}, 'WDC WD20PURZ-85GU6Y0': {'model': 'WDC WD20PURZ-85GU6Y0', 'manufacturer': '', 'total_size': '1863.01GB', 'interface': 'SCSI'}, 'SAMSUNG SP1614C': {'model': 'SAMSUNG SP1614C', 'manufacturer': '', 'total_size': '149.05GB', 'interface': 'SCSI'}}, 'HDD logical': {'C:\\': {'model': '', 'manufacturer': '', 'total_size': '231.81GB', 'interface': 'rw,fixed'}, 'D:\\': {'model': '', 'manufacturer': '', 'total_size': '111.69GB', 'interface': 'rw,fixed'}, 'E:\\': {'model': '', 'manufacturer': '', 'total_size': '1269.53GB', 'interface': 'rw,fixed'}, 'F:\\': {'model': '', 'manufacturer': '', 'total_size': '593.36GB', 'interface': 'rw,fixed'}, 'G:\\': {'model': '', 'manufacturer': '', 'total_size': '498.05GB', 'interface': 'rw,fixed'}, 'I:\\': {'model': '', 'manufacturer': '', 'total_size': '48.83GB', 'interface': 'rw,fixed'}, 'K:\\': {'model': '', 'manufacturer': '', 'total_size': '605.47GB', 'interface': 'rw,fixed'}, 'L:\\': {'model': '', 'manufacturer': '', 'total_size': '759.5GB', 'interface': 'rw,fixed'}, 'O:\\': {'model': '', 'manufacturer': '', 'total_size': '100.22GB', 'interface': 'rw,fixed'}, 'S:\\': {'model': '', 'manufacturer': '', 'total_size': '953.87GB', 'interface': 'rw,fixed'}}, 'Username': 'FeNix', 'domenname': 'FeNix-COMP', 'start_time': '2023-09-12 22:04:56', 'NET': {'IPv6 1': 'fe80::e5de:9c3e:ab7c:550', 'IPv6 2': '2a00:1370:8176:6f8:e9e5:d85f:202a:3c22', 'IPv6 3': '2a00:1370:8176:6f8:ac32:be6a:24cd:512d', 'IPv6 4': '2a00:1370:8176:6f8:2778:f763:8f1b:449f', 'IPv4 5': '192.168.1.67'}, 'time_start': '2023.09.16_15:40:47'}

    try:
        # # Конвертируем словарь в строку
        # str_dict = str(dict_info)
        #
        # # Кодируем строку в формат base64
        # base64_encoded = base64.b64encode(str_dict.encode('utf-8')).decode('utf-8')
        #
        # filename = 'file.txt'
        # # Записываем закодированную строку в файл
        # with open(filename, 'w') as file:
        #     file.write(base64_encoded)
        #     print(type(file))

        # мой токен
        YANDEX_TOKEN = "y0_AgAAAAABJQnxAAkufQAAAADiFPV_TjOFwUIbR6KNgvJ5KSFpjefPkow"
        # Инициализация объекта YaDisk
        disk = WorkingYandexDisk(YANDEX_TOKEN)
            # disk.upload(file, "/STATISTIC/file.txt", overwrite=True)

        # Конвертация словаря в строку и кодирование в base64
        encoded_str = base64.b64encode(str(dict_info).encode()).decode()

        # Создание BytesIO объекта с содержимым файла в формате base64
        file_contents = BytesIO(encoded_str.encode())

        # Загрузка содержимого файла на Яндекс Диск
        disk.upload_of_yd(
            filename=None,
            file_obj=file_contents,
            folder_name='109.252.8.126'
        )
        print('файл записан')

    except Exception as ex:
        print(ex)

def main():
    test()

if __name__ == '__main__':
    main()
