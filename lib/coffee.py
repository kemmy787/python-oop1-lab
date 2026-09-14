class Coffee:
    def __init__(self, size="Medium", status="hot", tip=0, price=0):
        # Trigger the property setter for validation
        self.size = size
        self.status = status
        self.tip = tip
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
        self._size = value

    def repair(self):
        print("the shoe has been repaired.")

    def add_1_to_price(self):
        self.price += 1

    def add_one_to_price(self):
        self.price += 1