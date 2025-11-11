
class Owner:
    def __init__(self, owner_id: int, first_name: str, last_name: str, phone_number: str) -> None:
        self.__owner_id = owner_id
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.__phone_number = phone_number.strip()
    
    def __str__(self) -> str:
        return f"Owner #{self.__owner_id}: {self.__first_name} {self.__last_name}\nphone number: {self.__phone_number}"
    
    def owner_id(self) -> int:
        return self.__owner_id
    
    def get_first_name(self) -> str:
        return self.__first_name
    
    def get_last_name(self) -> str:
        return self.__last_name
    
    def get_phone_number(self) -> str:
        return self.__phone_number
    
    def set_owner_id(self, owner_id: int) -> None:
        if isinstance(owner_id, int):
            if owner_id > 0:
                self.__owner_id = owner_id
            else:
                raise ValueError("Owner ID must be a positive intefer")
        else:
            raise TypeError("Owner ID must be an integer")
             
    def set_first_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("First name cannot be empty")
        self.__first_name = name.strip()
        
    def set_last_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Last name cannot be empty")
        self.__last_name = name.strip()

    def set_phone_number(self, number: str) -> None:
        if not number:
            raise ValueError("Phone number may not be empty")
        self.__phone_number = number.strip()

    
    def __eq__(self, other_name) -> bool:
        if not isinstance(other_name, Owner):
            return False
        return self.__owner_id == other_name.__owner_id
    
    @staticmethod
    def to_owner(row: list[str]):
        owner_id = int(row[0])
        first_name = str(row[1])
        last_name = str(row[2])
        phone_number = str(row[3])
        
        return Owner(owner_id, first_name, last_name, phone_number)
    
    def to_list(self) -> list[str]:
        output = []
        output.append(str(self.__owner_id))
        output.append(str(self.__first_name))
        output.append(str(self.__last_name))
        output.append(str(self.__phone_number))
        return output