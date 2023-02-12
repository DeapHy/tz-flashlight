class Flashlight:
    '''Класс "Фонарь"'''
    def __init__(self, state=False, color=16777215) -> None:
        '''Создает объект класса "Фонарь"
        - state: bool -- Состояние фонара (True - включен, False - выключен);
        - color: int -- Цвет фонаря (в диапазоне [0; 16777215])'''
        if color > 16777215 or color < 0:
            raise ValueError("Ошибка создания фонаря: значение цвета не лежит в диапазоне [0; 16777215]")
        self.__state = state
        self.__color = color

        # Список доступных команд
        self.__commandList = {
            "ON": self.on,
            "OFF": self.off,
            "COLOR": self.color,
        }
        print(f"Новый фонарь создан\n{self}")
    
    
    def __repr__(self) -> str:
        return f"Состояние фонаря: {'включен' if self.__state == True else 'выключен'}\nЦвет: {hex(self.__color)}"
    
    
    def on(self, *args) -> None:
        '''Включить фонарь'''
        if self.__state == True:
            print("Фонарь уже включен")
            return
        self.__state = True
        print("Состояние фонаря изменено на 'Включен'")


    def off(self, *args) -> None:
        '''Выключить фонарь'''
        if self.__state == False:
            print("Фонарь уже выключен")
            return
        self.__state = False
        print("Состояние фонаря изменено на 'Выключен'")


    def color(self, *args) -> None:
        '''Изменить цвет фонаря
        - color: int -- Новый цвет (в диапазоне [0; 16777215])
        '''
        color = args[0]
        if color > 16777215 or color < 0:
            print("Ошибка смены цвета фонаря: значение нового цвета не лежит в диапазоне [0; 16777215]")
            return
        self.__color = hex(color)
        print(f"Цвет фонаря изменен на {hex(color)}")


    def execute(self, payload: dict) -> None:
        '''Выполнить команду
        payload: {"command": text, "metadata": int | None} -- Выполняемая команда
        '''
        try:
            self.__commandList[payload["command"]](payload["metadata"])
        except KeyError:
            pass
