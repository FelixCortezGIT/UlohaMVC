from Shoe import Shoe

class ShoeModel:
    def __init__(self):
        self.shoes = []
    def add_shoe(self, shoe):
        self.shoes.append(shoe)
    def get_all(self):
        return self.shoes
    def remove_by_id(self, shoe_id):
        self.shoes = [s for s in self.shoes if s.id != shoe_id]
    def find_by_size(self, size):
        return [s for s in self.shoes if s.size == size]
    def total_price(self):
        return sum(s.price for s in self.shoes)
    def exists(self, shoe_id):
        return any(s.id == shoe_id for s in self.shoes)
