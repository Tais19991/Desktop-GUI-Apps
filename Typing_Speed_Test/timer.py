import math


class Timer:
    def __init__(self):
        self.work_min = 1
        self.work_sec = int(self.work_min * 60)

    def reset_timer(self) -> None:
        """Reset timer to initial state"""
        self.work_sec = int(self.work_min * 60)

    def count_down(self) -> tuple:
        """Count down seconds and show on window"""

        count_min = math.floor(self.work_sec / 60)
        count_sec = self.work_sec % 60
        if count_sec < 10:
            count_sec = '0' + f'{count_sec}'
        self.work_sec -= 1

        return count_min, count_sec

