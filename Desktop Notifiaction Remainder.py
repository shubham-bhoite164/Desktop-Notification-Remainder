
import time
from plyer import notification
if __name__ == '__main__':
    a = int(input())  # user can give input time
    while True:
        notification.notify(
        title = "All Day Remainder",
        message = "Today I have to submit my assignment",
        timeout = 10   # Time out is always in seconds
        )
        time.sleep(a)     # after how much time it'll repeat
