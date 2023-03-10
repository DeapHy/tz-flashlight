import asyncio
import websockets

from asyncio.exceptions import TimeoutError
from json import loads
from socket import gaierror
from tz_flashlight.flashlight import Flashlight
from websockets.exceptions import ConnectionClosedError

async def main(host="localhost", port=9999):
    try:
        # Подключение к серверу через WS
        async with websockets.connect(f"ws://{host}:{port}") as websocket:
            print("Соединение установлено")
            
            # Создание экземпляра класса "Фонарь"
            flashlight = Flashlight(True, 1111)

            while True:
                # Ожидание команды от сервера
                data: str = await websocket.recv()

                # Преобразование в dict
                data = loads(data)

                # Отправка команды на выполнение
                flashlight.execute(data)

    except ConnectionClosedError:
        print("Соединение с сервером потеряно")

    except (ConnectionRefusedError, TimeoutError):
        print("Невозможно соединиться с сервером")

    except gaierror:
        print("Адрес сервера имеет неверный формат")
        
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    # Запуск 
    asyncio.run(main())