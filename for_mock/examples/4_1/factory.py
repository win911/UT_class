# factory.py

class BadProductQualityError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # For python3
        # super(BadProductQuality, Exception).__init__(*args, **kwargs) # For python2

class Product():
    def __init__(self, quality_checker):
        self.quality_checker = quality_checker
        self.color = "Red"
        self.smell = "Rose"
        self.length = 10
        self.width = 10
        self.height = 10

    def create(self):
        pass

    def check_quality(self):
        if self.quality_checker.checkpoint_1(self.length, self.width, self.height) < 95:
            raise BadProductQualityError("Shape")
        if self.quality_checker.checkpoint_2(self.color) < 90:
            raise BadProductQualityError("Color")
        if self.quality_checker.checkpoint_3(self.smell) < 98:
            raise BadProductQualityError("Smell")