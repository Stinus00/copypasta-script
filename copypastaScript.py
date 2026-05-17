#!/usr/bin/env python

from random import randrange
import os
import keyboard
import pyperclip
import threading
import tkinter as tk
# This script randomly selects a line from a text file containing copypastas
# and copies it to the clipboard when Ctrl+A is pressed.

__location__ = os.path.abspath("../../copypastas.txt")

line_count = 0
x = "stopScript"

with open(__location__, 'r') as file:
    content = file.readlines()
    for line in content:
        if x in line:
            break
        line_count += 1

    rand_line = randrange(line_count)
    copypasta = content[randrange(line_count)].replace("\n", '')
    pyperclip.copy(copypasta)

prev_cycle = False

def start_blinking():
    def stop_script():
        print("Stopping script...")
        os._exit(0)  # Force exit all threads and main loop

    root = tk.Tk()
    root.title("Copypasta Script")
    root.geometry("250x100+0+20")  # Open in top left corner
    root.attributes("-topmost", True)  # Keep window always on top

    label = tk.Label(root, text="Script is running!", font=("Arial", 16))
    label.pack(expand=True)

    stop_btn = tk.Button(root, text="Stop", font=("Arial", 12), command=stop_script, bg="red", fg="white")
    stop_btn.pack(pady=5)

    def blink():
        current = label.cget("foreground")
        label.config(foreground="red" if current == "black" else "black")
        root.after(500, blink)

    blink()
    root.mainloop()

# Start the blinking window in a separate thread
threading.Thread(target=start_blinking, daemon=True).start()

print("Copypasta script started. Press Ctrl+A to copy, End to stop.")

def my_wait():
    keyboard.read_key()

def cycle_pasta():
    copypasta = content[randrange(line_count)].replace("\n", '')
    pyperclip.copy(copypasta)

def stop_script():
    print("Stopping script...")
    quit()

keyboard.add_hotkey("ctrl+a", cycle_pasta)
keyboard.add_hotkey("end", stop_script)

while True:
    my_wait()