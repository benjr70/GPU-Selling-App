class items:
    def __init__(self, name, price, MemSize, Chipset, pic, description):
        self.set_name(name)
        self.set_price(price)
        self.set_MemSize(MemSize)
        self.set_Chipset(Chipset)
        self.set_pic(pic)
        self.set_description(description)

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

    def set_description(self, description):
        self.__description = description
        
    def get_description(self):
        return self.__description
