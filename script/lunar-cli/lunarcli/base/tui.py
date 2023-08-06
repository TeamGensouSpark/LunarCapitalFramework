from abc import ABC,abstractmethod
from typing import Union


currentScreen = None

class ScreenBase(ABC):
    superscreen:Union["ScreenBase",None]
    def __init__(self,superscreen:Union["ScreenBase",None]) -> None:
        super().__init__()
        self.superscreen=superscreen
        global currentScreen
        currentScreen=self
    @abstractmethod
    def draw(self) -> None:
        ...

    def back(self) -> None:
        if self.superscreen != None:
            self.superscreen.draw()