from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Clothes(ClothesAbstract):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, clothes_item):
        self.items.append(clothes_item)

    @property
    def tissue_consumption(self):
        ctc = 0
        for item in self.items:
            ctc += item.tissue_consumption
        return ctc


class Coat(ClothesAbstract):
    def __init__(self, volume):
        self.volume = volume

    @property
    def tissue_consumption(self):
        return self.volume / 6.5 + 0.5


class Suit(ClothesAbstract):
    def __init__(self, height):
        self.height = height

    @property
    def tissue_consumption(self):
        return self.height * 2 + 0.3
