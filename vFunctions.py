# ⬡ CK42X · ck42x.com
# MODULE: spoken phrase triggers and fullscreen text display
# gold on black. sting once.

import tkinter as tk

def display_on_projector(text, screen_number=1):
    """fullscreen black window with white 24pt text; x offset in px is screenwidth * screen_number.
    TRAP: returns without mainloop; the window never pumps events."""
    root = tk.Tk()
    root.attributes('-fullscreen', True)

    root.geometry(f"+{root.winfo_screenwidth() * screen_number}+0")

    label = tk.Label(root, text=text, font=("Arial", 24), fg="white", bg="black")
    label.pack(expand=True)

def close_voice_to_text_screen(event):
        """escape destroys the projector window.
        TRAP: root and on_key_press are undefined in this scope.
        TRAP: check_phrases calls this with zero args."""
        if event.keysym == 'Escape':
            root.destroy()

            root.bind('<KeyPress>', on_key_press)

            root.mainloop()

# SAFETY: this call runs at import time; importing vFunctions opens a fullscreen window.
display_on_projector("Hello, this is being projected!", screen_number=1)



def displayText():
    """print the phrase 1 trigger line to stdout."""
    print("Function One triggered by Phrase 1!")



def check_phrases(transcription):
    """dispatch display/close triggers from a transcription.
    TRAP: uppercase needles are matched against a lowercased haystack; neither branch can fire."""
    if "Display Arc Text" in transcription.lower():
        displayText()

    if "Close Audio to Text Screen" in transcription.lower():
        close_voice_to_text_screen()
    