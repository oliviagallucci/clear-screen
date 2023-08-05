import platform
import os

 def clear_screen():
        system = platform.system()
        if system == 'Windows':
            os.system('cls')

        elif system == 'Linux' or system == 'Darwin':
            os.system('clear')
        else:
            # unsupported OS
            print("Unsupported OS - feel free to add support for this OS at ")
            print("https://github.com/oliviagallucci/clear-screen/")
            return
          
