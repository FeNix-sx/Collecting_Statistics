import time


def delay_print(text: str, func=print, sleep_time: float = 0.015, end: str='\n') -> None:
    try:
        for i in text:
            func(i, end='', flush=False)
            time.sleep(sleep_time)
        print(end=end)

    except Exception as ex:
        print(ex)