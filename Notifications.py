from win10toast import ToastNotifier
import time


def notification(title, message):
    toaster = ToastNotifier()
    toaster.show_toast(
        title,
        message,
        icon_path=None,
        duration=7)


if __name__ == "__main__":
    while True:
        notification("Break Time", "It's time to have a break.")
        time.sleep(1200)  # 20 minutes