from ShoeModel import ShoeModel
from Shoe import Shoe
from ShoeView import ShoeView

class ShoeController:
    def __init__(self):
        self.model = ShoeModel()
    def add_shoe(self, id, gender_type, type, color, brand, size):
        shoe = Shoe(id, gender_type, type, color, brand, size)
        self.model.add_shoe(shoe)
    def show_all(self):
        ShoeView.show_shoes(self.model.get_all())
