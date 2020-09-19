from .fighter import Fighter


class KarateFighter(Fighter):
    """
    Класс бойца Каратэ, наследует класс Fighter
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __str__(self):
        return self.name + " (Каратист)"
