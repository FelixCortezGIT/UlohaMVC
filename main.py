from ShoeController import ShoeController
from ShoeModel import ShoeModel
from ShoeView import ShoeView

controller = ShoeController()
model = ShoeModel()
view = ShoeView()

controller.add_shoe(1, "M", "tenisky", "biela", 89.90, "Nike", 42)
controller.add_shoe(2, "F", "sandale", "cierna", 39.9, "Adidas", 38)
controller.add_shoe(3, "M", "topanky", "hneda", 79.9, "Puma", 43)
controller.add_shoe(4, "F", "lodicky", "cervena", 59.9, "CCC", 37)
controller.add_shoe(5, "M", "tenisky", "modra", 99.9, "Nike", 44)
controller.add_shoe(6, "F", "tenisky", "biela", 74.9, "Reebok", 39)
controller.add_shoe(7, "M", "cizmy", "cierna", 129.9, "Timberland", 42)
controller.add_shoe(8, "F", "baleriny", "ruzova", 34.9, "Deichmann", 36)
controller.add_shoe(9, "M", "slapky", "zelena", 19.9, "Puma", 41)
controller.add_shoe(10, "F", "tenisky", "siva", 89.9, "Nike", 40)

controller.show_all()

print("\nzobrazujem velkost 42")
controller.show_by_size(42)

print()
controller.show_total_price()

controller.remove_shoe(3)

print()
controller.show_all()
