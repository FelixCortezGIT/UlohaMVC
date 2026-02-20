from Shoe import Shoe

class ShoeModel:
    def __init__(self):
        self.shoes = []
    def add_shoe(self, shoe):
        self.shoes.append(shoe)
    def get_all(self):
        return self.shoes
