import csv
from typing import Optional
from property import Property
from owner import Owner
from buyer import Buyer

class PropertyRepository:
    def __init__(self, filename: str = "property.csv") -> None:
        self.__filename = filename
        self.__properties = []
    
    def read_properties(self) -> list[Property]:
        properties: list[Property] = []
        with open(self.__filename, "r") as file:
            reader = csv.reader(file, delimiter=";")
        
            for row in reader:
                if not row:
                    continue
                properties.append(Property.to_property(row))
        return properties
    
    def save_property(self, properties: list[Property]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            for property in properties:
                writer.writerow(property.to_list())
    
    def add_property(self, address: str, price: float, sqr_foot: int, num_beds: int, owner_id: Optional[int] = None) -> None:
        properties = self.read_properties()
        if not properties:
            new_id = 1
        else:
            new_id = properties[-1].property_id() + 1
        new_property = Property(new_id, address, price, sqr_foot, num_beds, owner_id, [])
        properties.append(new_property)
        self.save_property(properties)
        print(f"Added: {new_property}\n")

    def update_property_price(self, id: int, new_price: float) -> bool:
        properties = self.read_properties()
        updated = False

        for property in properties:
            if property.property_id() == id:
                property.set_price(new_price)
                updated = True
                break
        
        if updated:
            self.save_property(properties)
        
        return updated

    def delete_property_by_id(self, id: int) -> bool:

        property_list = self.read_properties()
        new_property_list = []
        count = len(property_list)
        for property in property_list:
            if property.property_id() != id:
                new_property_list.append(property)
        
        if len(new_property_list) < count:
            self.save_property(new_property_list)
            return True
        else:
            return False
        
    def add_interested_buyer(self, property_id: int, buyer_id: int): 
        properties = self.read_properties() 
        changed = False 
        for prop in properties: 
            if prop.property_id() == property_id: 
                prop.add_buyer_id(buyer_id) 
                changed = True 
                break 

        if changed: 
            self.save_property(properties) 
        return changed 


    def remove_buyer_interest(self, property_id: int, buyer_id: int) -> bool: 
        properties = self.read_properties() 
        changed = False 
        for prop in properties: 
            if prop.property_id() == property_id: 
                prop.remove_buyer_id(buyer_id) 
                changed = True 
                break 
        if changed: 
            self.save_property(properties) 
        return changed
    
    def assign_owner_to_property(self, property_id: int, owner_id: int) -> bool:
        properties = self.read_properties()
        updated = False

        for prop in properties:
            if prop.property_id() == property_id:
                if prop.owner_id() is None:
                    prop.set_owner_id(owner_id)
                    updated = True
                    break   
        if updated:
            self.save_property(properties)

        return updated


class OwnerRepository:
    def __init__(self) -> None:
        self.__filename = "owner.csv"
    
    def read_owners(self) -> list[Owner]:
        owners: list[Owner] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
        
            for row in reader:
                if not row:
                    continue
                owners.append(Owner.to_owner(row))
        return owners
    
    def save_owner(self, owners: list[Owner]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            for owner in owners:
                writer.writerow(owner.to_list())
    
    def add_owner(self, first_name: str, last_name: str, phone_number: str) -> None:
        owners = self.read_owners()
        if not owners:
            new_id = 1
        else:
            new_id = owners[-1].owner_id() + 1

        new_owner = Owner(new_id, first_name, last_name, phone_number)
        owners.append(new_owner)
        self.save_owner(owners)
        print(f"Added: {new_owner}\n")

class BuyerRepository:
    def __init__(self) -> None:
        self.__filename = "buyer.csv"

    
    def read_buyers(self) -> list[Buyer]:
        buyers: list[Buyer] = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
        
            for row in reader:
                if not row:
                    continue
                buyers.append(Buyer.to_buyer(row))
        return buyers
    
    def save_buyer(self, buyers: list[Buyer]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            for buyer in buyers:
                writer.writerow(buyer.to_list())


    def add_buyer(self, first_name: str, last_name: str, phone_number: str) -> None:
        buyers = self.read_buyers()
        if not buyers:
            new_id = 1
        else:
            new_id = buyers[-1].buyer_id() + 1
        new_buyer = Buyer(new_id, first_name, last_name, phone_number)
        buyers.append(new_buyer)
        self.save_buyer(buyers)
        print(f"Added: {new_buyer}\n")

