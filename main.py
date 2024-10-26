"""This will launch the CLI version of the tool."""

from tools import CliMenu
from pyinputplus import inputYesNo

def main():
    """The entry point"""
    
    menu = CliMenu()
    
    clear_screen = inputYesNo("Hey there! Would you like me to clear the screen after menu use? (y/n) [Will prompt each time]\n:", postValidateApplyFunc=lambda x: x == 'yes')
    
    # The while loop!
    while True:
        # Display the menu!
        
        menu.display_menu()
        print("---")
        if clear_screen:
            input("Press enter to clear screen.")
    

if __name__ == "__main__":
    main()