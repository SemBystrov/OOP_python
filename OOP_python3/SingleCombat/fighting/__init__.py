"""
Лабораторная работа №2. Поединок
Выполнил: Быстров Семён, группа К33202

Содержит несколько классов бойцов и класс арены для поединков,
uml диаграмма в fighting.png
"""

from .arena import Arena
from .fighter import Fighter
from .karate import KarateFighter
from .taekwondo import TaekwondoFighter

fighter_classes = ['Каратэ', 'Тхэквондо']
fighter_factory = [
    lambda name: KarateFighter(name),
    lambda name: TaekwondoFighter(name)
]