
class Buyer:
    def __init__(self, buyer_id: int, first_name: str, last_name: str, phone_number: str) -> None:
        self.__buyer_id = buyer_id
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.__phone_number = phone_number.strip()
    
    def __str__(self) -> str:
        return f"Buyer #{self.__buyer_id}: {self.__first_name} {self.__last_name}\nphone number: {self.__phone_number}"
    
    def buyer_id(self) -> int:
        return self.__buyer_id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def phone_number(self) -> str:
        return self.__phone_number
    
    @first_name.setter
    def first_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("First name cannot be empty")
        self.__first_name = name.strip()
        
    @last_name.setter
    def last_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Last name cannot be empty")
        self.__last_name = name.strip()

    @phone_number.setter
    def phone_number(self, number: str) -> None:
        if not number:
            raise ValueError("Phone number may not be empty")
        self.__phone_number = number.strip()

    
    def __eq__(self, other_name) -> bool:
        if not isinstance(other_name, Buyer):
            return False
        return self.__buyer_id == other_name.__buyer_id
    
    @staticmethod
    def to_buyer(row: list[str]):
        buyer_id = int(row[0])
        first_name = str(row[1])
        last_name = str(row[2])
        phone_number = str(row[3])
        
        return Buyer(buyer_id, first_name, last_name, phone_number)
    
    def to_list(self) -> list[str]:
        output = []
        output.append(str(self.__buyer_id))
        output.append(str(self.__first_name))
        output.append(str(self.__last_name))
        output.append(str(self.__phone_number))
        return output