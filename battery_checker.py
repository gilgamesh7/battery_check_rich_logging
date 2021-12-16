import psutil
import logging
from rich.logging import RichHandler

from typing import Tuple

import tkinter as tk
from tkinter import messagebox

logging.basicConfig(level=logging.INFO, format="[{asctime}] - {funcName} - {message}", style='{', handlers=[RichHandler()])
logger=logging.getLogger("battery_checker")

def initialise()-> tk:
    try:
        # raise Exception("This is a test")
        root = tk.Tk()
        root.withdraw()

        return root
    except Exception as err:
        logger.error(f"Intialisation [red]failed[/red] with [bold purple]{err}[/bold purple]", extra={"markup": True})
        raise err

def get_info()-> Tuple[str,str,str]:
    battery = psutil.sensors_battery()
    
    return getattr(battery,"secsleft"), getattr(battery, "percent"), getattr(battery, "power_plugged")

def display_stats(root: tk, time_left: str, percentage: str, plugged:str)-> None:
    plugged_status = " not " if not plugged else ""
    display_message = (f"Battery Percent is at {percentage}%.\n"
                         f"You have {time_left/60/60:.1f} hours left.\n" 
                         f"Your computer is {plugged_status} plugged in.")
    messagebox.showinfo(message=display_message, parent=root)

if __name__ == "__main__":
    try:
        root = initialise()

        time_left, percentage, plugged = get_info()
        logger.info(f"{time_left} - {percentage} - {plugged}")

        display_stats(root, time_left, percentage, plugged)
       
    except Exception as err:
        logger.exception(f"Intialisation [red]failed[/red] with [bold purple]{err}[/bold purple]", extra={"markup": True})
