# Implemented in Python 3.7
from dataclasses import dataclass


# Regular method of class declaration
class InventoryItemRegular:
    def __init__(self, name: str, unit_price: float,
                 quantity_on_hand: int = 0) -> None:
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand


# Using @dataclass - totally equivalent to regular declaration
@dataclass
class InventoryItemDataClass:
    name: str  # Specify the type
    unit_price: float
    quantity_on_hand: int = 0  # Default value


obj_regular = InventoryItemRegular('rope', 5.99, quantity_on_hand=2)
print(obj_regular)

# Dataclass
obj_dataclass = InventoryItemDataClass('bottle', 1.99, quantity_on_hand=1)

# @dataclass defines __repr__
print(obj_dataclass)
