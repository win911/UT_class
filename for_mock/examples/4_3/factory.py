# factory.py

from random import randint


class BadProductQualityError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # For python3
        # super(BadProductQuality, Exception).__init__(*args, **kwargs) # For python2


class ProductQualityChecker():
    @staticmethod
    def checkpoint_1(length, width, height):
        return randint(1, 100)

    @staticmethod
    def checkpoint_2(color):
        return randint(1, 100)

    @staticmethod
    def checkpoint_3(smell):
        return randint(1, 100)


class Product():
    def __init__(self):
        self.color = "Red"
        self.smell = "Rose"
        self.length = 10
        self.width = 10
        self.height = 10

    def create(self):
        pass

    def check_quality(self):
        if ProductQualityChecker.checkpoint_1(self.length, self.width, self.height) < 95:
            raise BadProductQualityError("Shape")
        if ProductQualityChecker.checkpoint_2(self.color) < 90:
            raise BadProductQualityError("Color")
        if ProductQualityChecker.checkpoint_3(self.smell) < 98:
            raise BadProductQualityError("Smell")