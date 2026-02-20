class ShoeView:
    def show_shoes(shoes):
        if not shoes:
            print("topanky nie su na sklade")
        for shoe in shoes:
            print(shoe)
