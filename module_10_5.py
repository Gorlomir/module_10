import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

# Линейное выполнение
# start_time = time.time()
# for file_name in file_names:
#     read_info(file_name)
# end_time = time.time()
# print(f"Время выполнения линейно: {end_time - start_time} секунд")

# Многопроцессный подход
if __name__ == '__main__':
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    print(f"Время выполнения многопроцессно: {end_time - start_time} секунд")





