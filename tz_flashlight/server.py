from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from typing import Union
from starlette.websockets import WebSocketDisconnect
from json import dumps

# Создание экземпляра сервера
app = FastAPI()

# Класс для обработки тела запроса при вызове команды
class Command(BaseModel):
    command: str
    metadata: Union[int, None] = None

# Выполнение команды, передаваемой в теле запроса
@app.post("/execute")
async def send(command: Command):
    try:
        await websocketGlobal.send_text(dumps(command.dict()))
        return "true"
    except RuntimeError:
        print("Вызов команды после закрытия соединения")

# Обработка подключения по WS
@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    try:
        global websocketGlobal
        await websocket.accept()
        websocketGlobal = websocket
        await websocket.receive_text()
        return "true"
    except WebSocketDisconnect:
        print("Клиент отключился")