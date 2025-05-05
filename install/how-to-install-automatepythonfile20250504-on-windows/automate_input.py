import tkinter as tk
import pyautogui
import time

class DraggableTypingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Draggable Typing Emulator")
        
        # Create a text box for input
        self.input_box = tk.Text(root, height=10, width=50)
        self.input_box.pack(pady=10)

        # Create a button to start typing
        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=10)

        # Create a label to act as a cursor
        self.cursor_label = tk.Label(root, text="Typing Here...", bg="lightblue", relief="solid", width=20)
        self.cursor_label.pack(pady=5)

        # Make the cursor label draggable
        self.cursor_label.bind("<Button-1>", self.start_drag)
        self.cursor_label.bind("<B1-Motion>", self.do_drag)

        # Store the initial position of the cursor label
        self.cursor_label_x = 0
        self.cursor_label_y = 0

    def start_drag(self, event):
        # Store the initial position of the cursor label
        self.cursor_label_x = event.x
        self.cursor_label_y = event.y

    def do_drag(self, event):
        # Move the cursor label
        x = self.cursor_label.winfo_x() - self.cursor_label_x + event.x
        y = self.cursor_label.winfo_y() - self.cursor_label_y + event.y
        self.cursor_label.place(x=x, y=y)

    def start_typing(self):
        # Get the text from the input box
        text_to_input = self.input_box.get("1.0", tk.END).strip()
        
        if not text_to_input:
            return  # Do nothing if the input box is empty

        # Move the cursor to the current position
        cursor_x = self.cursor_label.winfo_x() + self.root.winfo_x()
        cursor_y = self.cursor_label.winfo_y() + self.root.winfo_y()

        # Move the mouse to the cursor position
        pyautogui.moveTo(cursor_x, cursor_y)

        # Type the text character by character
        for char in text_to_input:
            pyautogui.typewrite(char)
            time.sleep(0.01)  # Adjust the delay to 10 milliseconds for faster typing

# Create the main window
root = tk.Tk()
app = DraggableTypingApp(root)

# Start the GUI event loop
root.mainloop()
