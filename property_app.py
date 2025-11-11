import time
from app_repository import PropertyRepository, OwnerRepository, BuyerRepository
from property import Property

class PropertyApp:
    def __init__(self) -> None:
        self.prop_repo = PropertyRepository()
        self.owner_repo = OwnerRepository()
        self.buyer_repo = BuyerRepository()

        
    def show_menu(self) -> None:
        print("---- MENU----")
        print(" 1. Add new property listing")
        print(" 2. Update property price")
        print(" 3. Delete a property listing")
        print(" 4. Search for property by owner's name")
        print(" 5. Display all listings alphabetically")
        print(" 6. Display buyer information (and their properties of interest)")
        print(" 7. Display list of potential buyers of a specific property")
        print(" 8. Add new owner")
        print(" 9. Add new buyer")
        print("10. Add buyer interest to a property")
        print("11. Assign owner to an unassigned property")
        print("12. Exit\n")
        print()
    
    def run(self) -> None:
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_property_user_input()
            elif choice == 2:
                self.update_property()
            elif choice == 3:
                 self.delete_property()           
            elif choice == 4:
                 self.search_by_owner()       
            elif choice == 5:
                 self.display_owner_alphabetically()         
            elif choice == 6:
                 self.display_buyer_info()
            elif choice == 7:
                 self.display_buyers_for_property()
            elif choice == 8:
                 self.add_owner()
            elif choice == 9:
                 self.add_buyer()
            elif choice == 10:
                 self.add_interested_buyer()
            elif choice == 11:
                 self.assign_owner_to_property()
            elif choice == 12:
                print("Exiting APP...")
                time.sleep(2)
                break

            else:
                print("\nPlease select from one of the menu items below: \n")


    def add_property_user_input(self) -> None:
        address = input("Address: ").strip()
        try:
            price = float(input("Price: ").strip())
            sqr_foot = int(input("Square footage: ").strip())
            num_beds = int(input("Number of bedrooms: ").strip())
        except:
            print("Invalid numeric input. cancelling input.\n")
            return
        owners = self.owner_repo.read_owners()
        owner_id = None
        if owners:
            answer = input("Assign an owner now? (y/n): ").strip().lower()
            if answer == "y":
                for o in owners:
                    print(o)
                try:
                    owner_id = int(input("Enter owner id to assign: ").strip())
                except ValueError:
                    owner_id = None
        print("\n")
        new_prop = self.prop_repo.add_property(address, price, sqr_foot, num_beds, owner_id)
        
    def update_property(self) -> None:
        try:
            prop_id = int(input("Property id to update: ").strip())
            new_price = float(input("Enter new price for the property: ").strip())
        except:
            print("invalid input.\n")
            return
        if self.prop_repo.update_property_price(prop_id, new_price):
            print(f"\nPrice of property #{prop_id} successfully updated to {new_price}")
        else: 
            print("Property was not found!")

    
    def delete_property(self) -> None: 
        try: 
            prop_id = int(input("Property id to delete: ").strip()) 
        except ValueError: 
            print("Invalid id.\n") 
            return 
        if self.prop_repo.delete_property_by_id(prop_id): 
            print("Property deleted.\n") 
        else: 
            print("Property not found.\n") 


    def search_by_owner(self) -> None: 
        name = input("Enter owner full name or partial name: ").strip().lower()
        
        all_owners = self.owner_repo.read_owners()
        all_properties = self.prop_repo.read_properties()

        owner_lookup = {owner.owner_id(): owner for owner in all_owners}

        results = []

        for property_obj in all_properties:
            owner_id = property_obj.owner_id()
            if owner_id is not None:
                owner = owner_lookup.get(owner_id)
                if owner:
                    full_name = owner.get_first_name() + " " + owner.get_last_name()
                    if name in full_name.lower():
                        results.append(property_obj)
        if not results:
            print("No properties found for that owner\n")
            return
        
        index = 0 
        while index < len(results):
            property_obj = results[index]
            print(property_obj)
            print()
            index += 1


        
    def display_owner_alphabetically(self) -> None: 
        owners = self.owner_repo.read_owners() 
        if not owners: 
            print("No owners found.\n") 
            return
        
        for i in range(len(owners)):
            for j in range(i + 1, len(owners)):
                o1_last = owners[i].get_last_name().lower()
                o2_last = owners[j].get_last_name().lower()
                if o1_last > o2_last:
                    temp = owners[i]
                    owners[i] = owners[j]
                    owners[j] = temp

        print("-----Owners (sorted alphabetically)-----")
        for owner in owners:
            print(owner)
        
        print() 
        
    
    def display_buyer_info(self) -> None: 
        buyers = self.buyer_repo.read_buyers() 
        if not buyers: 
            print("No buyers found.\n") 
            return 
        for b in buyers: 
            print(b) 
        print()

        try: 
            bid = int(input("Enter buyer id to show their interested properties (or 0 to skip): ").strip()) 
        except ValueError: 
            print("Invalid id\n")
            return 
        if bid == 0: 
            return 
        properties = self.prop_repo.read_properties() 
        interested = []
        for p in properties:
            if bid in p.buyer_ids():
                interested.append(p)
        if not interested: 
            print("This buyer is not interested in any properties.\n") 
            return 
        print("Buyer is interested in:") 
        for p in interested: 
            print(p) 
            print() 
            
    def display_buyers_for_property(self) -> None: 
        try: 
            prop_id = int(input("Enter property id: ").strip()) 
        except ValueError: 
            print("Invalid id.\n") 
            return 
        properties = self.prop_repo.read_properties() 
        target = None
        for p in properties:
            if p.property_id() == prop_id:
                target = p
                break


        if not target: 
            print("Property not found.\n") 
            return 
        
        buyer_ids = target.buyer_ids() 
        if not buyer_ids: 
            print("No buyers have expressed interest in this property.\n")
            return 
        
        buyers = self.buyer_repo.read_buyers() 
        buyers_lookup = {}
        for b in buyers:
            buyers_lookup[b.buyer_id()] = b

        for bid in buyer_ids: 
            b = buyers_lookup.get(bid) 
            if b: 
                print(b) 
            else: 
                print(f"Buyer id {bid} (record not found)") 
        print() 
            
    def add_interested_buyer(self) -> None: 
        try: 
            prop_id = int(input("Enter property id: ").strip()) 
            buyer_id = int(input("Enter buyer id: ").strip()) 
        except ValueError:
            print("Invalid id input\n")
            return
        
        buyers = self.buyer_repo.read_buyers() 
        buyer_found = False
        for b in buyers:
            if b.buyer_id() == buyer_id:
                buyer_found = True
                break

        if not buyer_found:
            print("Buyer id not found.\n") 
            return 
        
        if self.prop_repo.add_interested_buyer(prop_id, buyer_id): 
            print("Buyer interest added.\n") 
        
        else: 
            print("Property not found.\n") 
        
    
    def add_owner(self) -> None: 
        first = input("Owner first name: ").strip() 
        last = input("Owner last name: ").strip() 
        phone = input("Owner phone: ").strip()
        print()
        owner = self.owner_repo.add_owner(first, last, phone) 
         
        
    def add_buyer(self) -> None: 
        first = input("Buyer first name: ").strip() 
        last = input("Buyer last name: ").strip() 
        phone = input("Buyer phone: ").strip() 
        print()
        buyer = self.buyer_repo.add_buyer(first, last, phone) 


    def assign_owner_to_property(self) -> None:
        all_properties = self.prop_repo.read_properties()
        unassigned_props = []

        for p in all_properties:
            if p.owner_id() is None:
                unassigned_props.append(p)
        
        if not unassigned_props:
            print("\nAll properties currently have an owner assigned.")
            return
        
        print("----- Unassigned Properties -----")
        for p in unassigned_props:
            print(f"ID: {p.property_id()} | Address: {p.address()}")
        print("--------------------------------\n")

        try:
            prop_id = int(input("Enter Property ID to assign an owner to: ").strip())
        
        except ValueError:
            print("Invalid Property ID.\n")
            return

        target_property = None
        for p in unassigned_props:
            if p.property_id() == prop_id:
                target_property = p
                break
        
        if target_property is None:
            print(f"Property ID {prop_id} not found or already has an owner")

        all_owners = self.owner_repo.read_owners()
        if not all_owners:
            print("No owners available to assign. Please add an owner first (Menu option 9)")
            return
        print("\n--- Available Owners ---")
        for o in all_owners:
            print(o)
        
        print("------------------------\n")

        try:
            owner_id = int(input("Enter Owner ID to assign to this property: ").strip())
        except ValueError:
            print("Invalid Owner ID")
            return

        owner_exists = False
        for o in all_owners:
            if o.owner_id() == owner_id:
                owner_exists = True
                break
        
        if not owner_exists:
            print("Owner ID not found")
            return
        
        if self.prop_repo.assign_owner_to_property(prop_id, owner_id):
            print(f"\nSuccessfully assigned owner #{owner_id} to property #{prop_id}\n")
        else:
            print("Update failed - Property not found\n")


if __name__ == "__main__":
    app = PropertyApp()
    app.run()
