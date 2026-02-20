class ShoeView:
    @staticmethod
    def show_shoes(shoes):
        if not shoes:
            print("topanky nie su na sklade")
            return
        for shoe in shoes:
            print(shoe)
    @staticmethod
    def show_total_price(price):
        print(f"celkova cena topanok: {price}£")
    @staticmethod
    def show_message(msg):
        print(msg)
