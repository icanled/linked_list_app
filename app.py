import PySimpleGUI as GUI
from linked_list import LinkedList

def main():
    ll = LinkedList()
    
    layout = [
        [GUI.Text("Linked List Visualiser", font=("Helvetica", 16, "bold"))],
        
        # Inputs
        [
            GUI.Text("Value:"),
            GUI.Input(key="-VAL-", size=(10, 1)),
            GUI.Text("Index (Optional):"),
            GUI.Input(key="-INDEX-", size=(6, 1))
        ],
        
        # Action Buttons
        [
            GUI.Button("Insert", key="-INSERT-"),
            GUI.Button("Delete", key="-DELETE-"),
            GUI.Button("Clear List", key="-CLEAR-"),
            GUI.Button("Exit", key="-EXIT-")
        ],
        
        [GUI.HorizontalSeparator()],
        
        # Visual Chain Display Section
        [GUI.Text("Current Linked List:", font=("Helvetica", 11, "bold"))],
        [GUI.Text("Empty (None)", key="-DISPLAY-", font=("Courier", 13))],
        
        # Status / Error Message Banner 
        [GUI.Text("", key="-STATUS-", size=(50, 1))]
    
    ]
    
    window = GUI.Window("Linked List Visualiser", layout, finalize=True)
    
    # Event Loop
    while True:
        event, values = window.read()
        
        if event in (GUI.WIN_CLOSED, "-EXIT-"):
            break
        
        if event == "-INSERT-":
            value = values["-VAL-"].strip()
            index_str = values["-INDEX-"].strip()
            
            if not value:
                window["-STATUS-"].update("❌ Value cannot be empty!")
                continue
            
            if index_str == "":
                success = ll.insert(value)
            else:
                try:
                    index = int(index_str)
                    success = ll.insert(value, index)
                except ValueError:
                    window["-STATUS-"].update("❌ Index must be a valid integer!")
                    continue
            
            if success:
                window["-STATUS-"].update(f"✅ Inserted '{value}' into list.")
                window["-VAL-"].update("")
                window["-INDEX-"].update("")
            else:
                window["-STATUS-"].update("❌ Insertion failed (index out of bounds).")
        
        elif event == "-DELETE-":
            value = values["-VAL-"].strip()
            
            if not value:
                window["-STATUS-"].update("❌ Enter a value in the 'Value' field to delete!")
                continue
            
            if ll.delete(value):
                window["-STATUS-"].update(f"✅ Deleted '{value}' from list.")
                window["-VAL-"].update("")
            else:
                window["-STATUS-"].update(f"❌ Value '{value}' not found in list.")
        
        elif event == "-CLEAR-":
            ll = LinkedList()
            window["-STATUS-"].update("List cleared.")
            
        elements = ll.to_list()
        if elements:
            visual_str = "(Head) " + " -> ".join([f"[ {item} ]" for item in elements]) + " -> None"
        else:
            visual_str = "Empty (None)"
        
        window["-DISPLAY-"].update(visual_str)
    
    window.close()

if __name__ == "__main__":
    main()