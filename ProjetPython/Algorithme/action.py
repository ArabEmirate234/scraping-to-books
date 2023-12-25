from typing import List

class Action:
    list_action: List = []

    def __init__(self, name, price, profit) -> None:
        self.price = price
        self.name = name
        self.profit = profit
        self.gain_in_euro = (price*profit)/100
        self.list_action.append(self)

    def __repr__(self) -> str:
        return self.name + ",  price : " + str(self.price) + " €, profit en euro : " + str(self.gain_in_euro) + "%"
    
class OAction:
    def __init__(self,name,price,profit):
        self.price = price
        self.name = name
        self.profit = profit
        self.gain = (self.price * self.profit) / 100
        self.profitability = (self.gain / self.price) * 100