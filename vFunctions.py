import tkinter as tk

def display_on_projector(text, screen_number=1):
    # Tkinter window
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Set the window to full-screen

    # Move the window to the projector screen
    root.geometry(f"+{root.winfo_screenwidth() * screen_number}+0")

    # Add a label with the specified text
    label = tk.Label(root, text=text, font=("Arial", 24), fg="white", bg="black")
    label.pack(expand=True)

    # Function to close the window when phrase is heard
def close_voice_to_text_screen(event):
        if event.keysym == 'Escape':
            root.destroy()

            root.bind('<KeyPress>', on_key_press)  # Bind the key press event

             # Start the application
            root.mainloop()

# Example usage
display_on_projector("Hello, this is being projected!", screen_number=1)



def displayText():
    print("Function One triggered by Phrase 1!")



#check for phrases 
def check_phrases(transcription):
    if "Display Arc Text" in transcription.lower():
        displayText()

    if "Close Audio to Text Screen" in transcription.lower():
        close_voice_to_text_screen()
    