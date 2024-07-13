import datetime
from dataclasses import dataclass

@dataclass
class Sale:
    Retailer_code:int
    Product_number:int
    Order_method_code:int
    Date:datetime.datetime
    Quantity:int
    Unit_price:float
    Unit_sale_price:float

    @property
    def retailer_code(self):
        return self.Retailer_code

    @property
    def date(self):
        return self.Date

    def __hash__(self):
        return hash(self.Retailer_code,self.Product_number,self.Date)