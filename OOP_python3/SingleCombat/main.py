import sys
from time import sleep
from PyQt5 import QtWidgets
import design
# Импорт моей библиотеки
from fighting import Arena, Fighter, fighter_classes, fighter_factory


class SingleCombatApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """
    Класс приложения
    """
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.class_p1_choose.addItems(fighter_classes)
        self.class_p2_choose.addItems(fighter_classes)
        self.start.clicked.connect(self.__app)

    def __app(self) -> None:
        # Закрываю выбор класса бойца
        self.class_p1_choose.setDisabled(True)
        self.class_p2_choose.setDisabled(True)

        # Обновляю и активирую текстовое поле
        self.fight_progress.clear()
        self.fight_progress.setDisabled(False)

        # Инициализирую арену и игроков
        fighter1: Fighter = fighter_factory[self.class_p1_choose.currentIndex()]("Player1")
        fighter2: Fighter = fighter_factory[self.class_p2_choose.currentIndex()]("Player2")
        arena: Arena = Arena(fighter1, fighter2)

        # Провожу поединок
        for f in arena.fight():
            # Отображаю новый ход
            self.fight_progress.append(f)

            sleep(0.2)

            # Отображаю здоровье бойцов
            self.hp_p1.setValue(fighter1.hp)
            self.hp_p2.setValue(fighter2.hp)

            # Задержка
            sleep(0.5)

        # Обновляю поля
        self.fight_progress.setDisabled(True)
        self.class_p1_choose.setDisabled(False)
        self.class_p2_choose.setDisabled(False)
        self.hp_p1.setValue(100)
        self.hp_p2.setValue(100)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SingleCombatApp()  # Создаю объект класса приложение
    window.show()  # Показываю окно
    app.exec_()  # и запуск приложения

