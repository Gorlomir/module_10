import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0

        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            time.sleep(1)
            with lock:
                print(f"{self.name} сражается {days} дней(дня), осталось {self.enemies} воинов.")

        with lock:
            print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

lock = threading.Lock()

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
