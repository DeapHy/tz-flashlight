import unittest

from tz_flashlight.client import Flashlight

class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyFlashlight = Flashlight()
        self.exactFlashlight = Flashlight(True, 15111)
        return super().setUp()

    def test_1(self) -> None:
        self.assertEqual(str(self.emptyFlashlight), "Состояние фонаря: выключен\nЦвет: 0xffffff")

    def test_2(self) -> None:
        self.assertEqual(str(self.exactFlashlight), "Состояние фонаря: включен\nЦвет: 0x3b07")

    def test_3(self) -> None:
        payload = {
            "command": "OFF",
            "metadata": None
        }
        self.exactFlashlight.execute(payload)
        self.assertEqual(str(self.exactFlashlight), "Состояние фонаря: выключен\nЦвет: 0x3b07")

    def test_4(self) -> None:
        payload = {
            "command": "ON",
            "metadata": None
        }
        self.exactFlashlight.execute(payload)
        self.assertEqual(str(self.exactFlashlight), "Состояние фонаря: включен\nЦвет: 0x3b07")

    def test_5(self) -> None:
        payload = {
            "command": "COLOR",
            "metadata": 1611141
        }
        self.exactFlashlight.execute(payload)
        self.assertEqual(str(self.exactFlashlight), "Состояние фонаря: включен\nЦвет: 0x189585")