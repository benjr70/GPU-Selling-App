class items:
    def __init__(self, name, price, MemSize, Chipset, pic):
        self.set_name(name)
        self.set_price(price)
        self.set_MemSize(MemSize)
        self.set_Chipset(Chipset)
        self.set_pic(pic)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_MemSize(self, MemSize):
        self.__MemSize = MemSize

    def get_MemSize(self):
        return self.__MemSize

    def set_Chipset(self, Chipset):
        self.__Chipset = Chipset

    def get_Chipset(self):
        return self.__Chipset

    def set_pic(self, pic):
        self.__pic = pic

    def get_pic(self):
        return self.__pic
