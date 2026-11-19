from linked_list import LinkedList

def main():
    ll = LinkedList()
    
    while True:
        current_elements = ll.to_list() 
        visual_str = " -> ".join(current_elements) + " -> None" if current_elements else "Empty (None)" ## inline if else
        
        print("\n" + "=" * 40) 
        print(" LINKED LIST TERMINAL TESTER") 
        print("=" * 40) 
        print(f"Current List: {visual_str}") 
        print("-" * 40) 
        print("1. Insert (Append, Prepend, or at Index)") 
        print("2. Delete Value") 
        print("3. View Full List") 
        print("4. Exit") 
        print("-" * 40)
        
        choice = input("Select option: ").strip()
        
        if choice == "1":
            val = input("Enter value to insert: ").strip()
            if not val:
                print("❌ Value cannot be empty!") 
                continue
            
            index_str = input("Enter index (Press ENTER to default append to end): ").strip()
            
            if index_str == "":
                success = ll.insert(val)
            else:
                try:
                    index = int(index_str)
                    success = ll.insert(val, index)
                except ValueError:
                    print("❌ Index must be a valid integer!")
                    continue
            
            if success:
                print(f"✅ Successfully inserted '{val}'!")
            else:
                print("❌ Insertion failed (invalid or out of bounds index).")
            
        elif choice == "2":
            val = input("Enter value to delete: ").strip()
            if ll.delete(val):
                print(f"✅ Successfully deleted '{val}'.")
            else:
                print(f"❌ Value '{val}' not found in the list.")
                    
        elif choice == "3":
            elements = ll.to_list()
            print("\n--- Visualizing Chain ---")
            if elements:
                for i, item in enumerate(elements):
                    print(f" [Index {i}]: Node({item})")
                print(" -> None")
            else:
                print(" The list is currently empty.")
                    
        elif choice == "4":
            print("\nExiting tester. Goodbye!")
            break
            
        else:
            print("❌ Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__": 
    main()