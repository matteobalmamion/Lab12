import datetime
from dataclasses import dataclass
@dataclass
class Connection:
    product:int
    retailer1:int
    retailer2:int

    def __hash__(self):
        return hash(str(self.product)+str(self.retailer1)+str(self.retailer2))