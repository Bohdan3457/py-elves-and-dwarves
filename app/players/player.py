from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nick_name: str) -> None:
        self.nick_name = nick_name

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
