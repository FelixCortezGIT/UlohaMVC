from ShoeController import ShoeController
from ShoeModel import ShoeModel
from ShoeView import ShoeView

controller = ShoeController()
model = ShoeModel()
view = ShoeView()

controller.add_shoe(1, "M", "tenisky", "biela", "Nike", 42)

controller.show_all()
