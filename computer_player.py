 
import os
import shutil
import time
import pyfiglet
from colorama import Fore, Style

def center_text(text):
    # Get the width of the terminal window
    terminal_width = shutil.get_terminal_size().columns
    
    # Calculate horizontal padding
    horizontal_padding = (terminal_width - len(text)) // 2
    
    # Calculate vertical padding
    vertical_padding = (shutil.get_terminal_size().lines - 1) // 2
    
    # Add padding and return centered text
    centered_text = '\n' * vertical_padding + ' ' * horizontal_padding + text
    return centered_text


def display_intro():
    os.system('clear')
    start_time = time.time()  # Record the start time
    duration = 3  # Duration of 3 seconds
    text = pyfiglet.figlet_format("P  I  G", font="big_money-se")
    color_codes = [getattr(Fore, color.upper(), Fore.WHITE) for color in ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]]
    while time.time() - start_time < duration:
        for color in color_codes:
            centered_text = center_text(text)  # Center the text
            print(color + centered_text + Style.RESET_ALL, end="\r", flush=True)
            time.sleep(0.3)
            os.system('clear')

display_intro()
