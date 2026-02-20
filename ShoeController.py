from ShoeModel import ShoeModel
from Shoe import Shoe
from ShoeView import ShoeView

class ShoeController:
    def __init__(self):
        self.model = ShoeModel()
    def add_shoe(self, id, gender_type, type, color, price, brand, size):
        if self.model.exists(id):
            ShoeView.show_message("topanky s tymto ID uz existuju")
            return
        if price < 0:
            ShoeView.show_message("cena nemoze byt mensia ako 0")
            return
        shoe = Shoe(id, gender_type, type, color, price, brand, size)
        self.model.add_shoe(shoe)
    def show_all(self):
        ShoeView.show_shoes(self.model.get_all())
    def remove_shoe(self, id):
        self.model.remove_by_id(id)
        ShoeView.show_message(f"topanky [{id}] boli odstranene")
    def show_by_size(self, size):
        ShoeView.show_shoes(self.model.find_by_size(size))
    def show_total_price(self):
        ShoeView.show_total_price(self.model.total_price())
