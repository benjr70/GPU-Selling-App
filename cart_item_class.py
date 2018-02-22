from Tkinter import *
from item_class import items

class cartItem:
    def __init__(self,Label, button, itemclass, quantity):
        self.set_label(Label)
        self.set_button(button)
        self.set_itemclass(itemclass)
        self.set_quantity(quantity)

    def set_label(self, label):
        self.__label = label
            
    def get_label(self):
        return self.__label

    def set_button(self, button):
        self.__button = button

    def get_button(self):
        return self.__button

    def set_itemclass(self, itemclass):
        self.__itemclass = itemclass

    def get_itemclass(self):
        return self.__itemclass

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity
