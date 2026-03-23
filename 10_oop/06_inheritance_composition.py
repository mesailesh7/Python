class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"{self.type} prepared")


class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"{self.type} spices added")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self, type_):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"{self.chai.type} served")
        self.chai.prepare()
