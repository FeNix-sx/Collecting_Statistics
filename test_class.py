def test():
    # Получить координаты и размеры рабочего стола
    screen_info = pyautogui.screen_info()
    x, y, width, height = screen_info['screen_left'], screen_info['screen_top'], screen_info['screen_width'], \
    screen_info['screen_height']

    # Создать скриншот рабочего стола
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    # Сохранить скриншот в файл
    screenshot.save('screenshot.png')

def main():
    test()

if __name__ == '__main__':
    main()
