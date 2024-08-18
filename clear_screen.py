"""
Help on clear-screen.py:

NAME
    clear_screen.py

DESCRIPTION
    clear-screen is a Python module that detects the host operating system
    and will clear a terminals text history when the clear_screen() function
    is called.

    See https://github.com/oliviagallucci/clear-screen for complete documentation

PACKAGE CONTENTS
    clear_screen()
"""
import os

def clear_screen():
   """
   clear_screen uses os.name to detect the operating system then
   uses os.system to execute the appropriate terminal command for clearing the screen

   Args:
       None
   Returns:
       Success == True
   """
   # https://github.com/python/cpython/blob/main/Lib/os.py#L6
   if os.name in ("nt", "dos", "ce"):
      os.system('cls')
   elif os.name == 'posix':
      os.system('printf "\033c"') # https://stackoverflow.com/questions/24754406/how-can-you-clear-reset-the-screen-in-unix-posix-not-curses-newlines
   else:
      print("Unsupported OS - feel free to add support for this OS at ")
      print("https://github.com/oliviagallucci/clear-screen/")
      return False
   return True

if __name__ == "__main__":
    """
    DESCRIPTION
        clear_screen.py: Detects the host operating system and clears a terminals text history

    CLI USAGE
        python3 clear_screen.py
    """
    clear_screen()
