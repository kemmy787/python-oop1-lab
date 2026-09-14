class Coffee:
    def __init__(self, size="Medium", status="hot", tip=0, price=0):
        self.size = size
        self.status = status
        self.tip = tip
        self._price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
        self._size = value

    def price(self, new_price=None):
        if new_price is not None:
            self._price = new_price
        return self._price

    def add_1_to_price(self):
        self._price += 1

    def repair(self):
        print("the shoe has been repaired.")