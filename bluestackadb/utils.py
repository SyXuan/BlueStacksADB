import sys
import time


class Utils:
    @staticmethod
    def count_down(seconds):
        print(f'Waiting for {seconds} seconds')
        for i in range(seconds, 0, -1):
            remaining = Utils.seconds_to_time(i)
            sys.stdout.write(f'\r{remaining} remaining')
            time.sleep(1)
        print("\r")

    @staticmethod
    def seconds_to_time(seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return f'{h}h:{m}m:{s}s'
