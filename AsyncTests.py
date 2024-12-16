import asyncio
import time

end_time = 0

async def database_query():
    await asyncio.sleep(2)
    print("Запрос выполнен")

async def user_interface():
    await asyncio.sleep(1)
    print("С интерфейсом можно взаимодействовать")

start_time = time.time()
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(user_interface())
        tg.create_task(database_query())
        tg.create_task(user_interface())

asyncio.run(main())
print(f"Время выполнения функции {time.time()- start_time}")