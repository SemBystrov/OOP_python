from .fighter import Fighter
from typing import Iterator, List
from random import randint


class Arena:
    """
    Класс арены на которой проходит бой
    fight - поединок между двумя переданными бойцами
    """
    def __init__(self, fighter1: Fighter, fighter2: Fighter) -> None:
        self.__fighters: List[Fighter] = [fighter1, fighter2]

    def fight(self) -> Iterator[str]:
        while self.__fighters[0].hp and self.__fighters[1].hp:
            # Определяю атакующего и обороняющегося бойца
            attacking: int = randint(0, 1)
            defending: int = abs(attacking - 1)

            # Атакующий боец наносит удар
            self.__fighters[attacking].hit(self.__fighters[defending])

            # Возвращаю информацию о ходе поединка
            yield str(self.__fighters[attacking]) + " ударил " + str(self.__fighters[defending])

        # Объявляю победителя
        if self.__fighters[0].hp == 0:
            yield "Победа за " + str(self.__fighters[1])
        else:
            yield "Победа за " + str(self.__fighters[0])
