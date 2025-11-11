# from buyer import Buyer
# from owner import Owner
from __future__ import annotations
from typing import Optional

class Property:
    def __init__(self, property_id: int, address: str, price: float, sqr_foot: int, num_beds: int,
                 owner_id: Optional[int] = None, buyer_ids: Optional[list[int]] = None) -> None:
        self.__property_id = property_id
        self.__address = address.strip()
        self.__price = float(price)
        self.__sqr_foot = int(sqr_foot)
        self.__num_beds = int(num_beds)
        self.__owner_id = owner_id
        self.__buyer_ids: list[int] = buyer_ids or []
        
    def __str__(self) -> str:
        if self.__owner_id is not None:
            owner_text = "Owner ID: " + str(self.__owner_id)
        else:
            owner_text = "Owner is not assigned"
        
        if self.__buyer_ids is not None and len(self.__buyer_ids) > 0:
            buyers_text = ""
            index = 0
            while index < len(self.__buyer_ids):
                buyers_text = buyers_text + str(self.__buyer_ids[index])
                if index < len(self.__buyer_ids) - 1:
                    buyers_text = buyers_text + ", "
                index += 1

        else:
            buyers_text = "No buyers are listed"
        
        result = ""
        result = result + "Property #" + str(self.__property_id) + "\n"
        result = result + "Address: " + self.__address + "\n"
        result = result + "Square Footage: " + str(self.__sqr_foot) + "\n"
        result = result + "Bedroons: " + str(self.__num_beds) + "\n"
        result = result + owner_text + "\n"
        result = result + "Price: $" + str(round(self.__price, 2)) + "\n"
        result = result + "Interested buyers: " + buyers_text

        return result


    def property_id(self) -> int:
        return self.__property_id
    
    def address(self) -> str:
        return self.__address
    
    def price(self) -> float:
        return self.__price
    
    def sqr_foot(self) -> int:
        return self.__sqr_foot
    
    def num_beds(self) -> int:
        return self.__num_beds
    
    def owner_id(self) -> Optional[int]:
        return self.__owner_id
    
    def buyer_ids(self) -> list[int]:
        return list(self.__buyer_ids)
    
    def set_price(self, new_price: float) -> None:
        if new_price is None:
            raise ValueError("Price may not be blank")
        self.__price = float(new_price)
    
    def set_owner_id(self, owner_id: Optional[int]) -> None:
        self.__owner_id = owner_id

    def add_buyer_id(self, buyer_id: int) -> None:
        if buyer_id not in self.__buyer_ids:
            self.__buyer_ids.append(buyer_id)

    def remove_buyer_id(self, buyer_id: int) -> None:
        if buyer_id in self.__buyer_ids:
            self.__buyer_ids.remove(buyer_id)

    
    @staticmethod
    def to_property(row: list[str]) -> "Property":
        property_id = int(row[0])
        address = row[1]
        price = float(row[2])
        sqr_foot = int(row[3])
        num_beds = int(row[4])

        owner_id = None
        if len(row) > 5:
            value = row[5].strip()
            if value != "":
                owner_id = int(value)
        
        buyer_ids = []
        if len(row) > 6:
            ids_string = row[6].strip()
            if ids_string != "":
                ids_list = ids_string.split()
                index = 0
                while index < len(ids_list):
                    id_value = ids_list[index].strip()
                    if id_value.isdigit():
                        buyer_ids.append(int(id_value))
                    index += 1



        return Property(property_id, address, price, sqr_foot, num_beds, owner_id, buyer_ids)
    
    def to_list(self) -> list[str]:
        output = []
        output.append(str(self.__property_id))
        output.append(str(self.__address))
        output.append(str(self.__price))
        output.append(str(self.__sqr_foot))
        output.append(str(self.__num_beds))

        if self.__owner_id is not None:
            output.append(str(self.__owner_id))
        else:
            output.append("")
        buyer_id_strings = []
        for bid in self.__buyer_ids:
            buyer_id_strings.append(str(bid))
        buyer_id_strings = " ". join(buyer_id_strings)
                    
        output.append(buyer_id_strings)

        return output
 
