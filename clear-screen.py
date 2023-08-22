import os

 def clear_screen():
        os_name = os.name # https://github.com/python/cpython/blob/main/Lib/os.py#L6
        if os_name == 'nt':
            os.system('cls')

        elif os_name == 'posix':
            os.system('printf "\033c"') # https://stackoverflow.com/questions/24754406/how-can-you-clear-reset-the-screen-in-unix-posix-not-curses-newlines
        else:
            # unsupported OS
            print("Unsupported OS - feel free to add support for this OS at ")
            print("https://github.com/oliviagallucci/clear-screen/")
            return
          
