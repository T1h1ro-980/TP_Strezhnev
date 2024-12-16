import time

def time_counter(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Время выполнения функции main: {end_time - start_time}")
    return wrapper 

def database_query():
    time.sleep(2)
    print("Запрос выполнен")

def user_interface():
    time.sleep(1)
    print("С интерфейсом можно взаимодействовать")

@time_counter
def main():
    user_interface()
    database_query()
    user_interface()

main()
