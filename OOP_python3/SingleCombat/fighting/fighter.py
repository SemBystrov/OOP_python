from __future__ import annotations


class Fighter:
    """
    Класс бойца:
    hp - количество здоровья
    name - имя бойца
    hit - удар бойца
    get_damaged - получение урона
    """
    def __init__(self, name: str) -> None:
        self.__hp: int = 100
        self.__power: int = 20
        self.__name: str = name

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def name(self) -> str:
        return self.__name

    def hit(self, fighter: Fighter) -> None:
        fighter.get_damaged(self.__power)

    def get_damaged(self, power: int) -> None:
        self.__hp -= power
